from flask import Flask, render_template, request, jsonify
from analyser import read_pdf, chunk_text, embed_chunks, get_top_k_chunks, parse_query_with_gemini, make_decision_with_gemini
from deep_translator import GoogleTranslator

from db import collection
import json, os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    pdf_file = request.files['policy_pdf']
    query = request.form['query']
    pdf_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
    pdf_file.save(pdf_path)

    # Step 1: Extract and embed
    text = read_pdf(pdf_path)
    chunks = chunk_text(text)
    chunk_vectors = embed_chunks(chunks)

    # Step 2: Parse and analyze
    parsed_output = parse_query_with_gemini(query)
    cleaned_output = parsed_output.strip().removeprefix("```json").removesuffix("```").strip()

    try:
        parsed_query = json.loads(cleaned_output)
    except:
        return jsonify({"error": "Failed to parse Gemini JSON", "raw": parsed_output})

    top_chunks = get_top_k_chunks(query, chunks, chunk_vectors)
    decision_raw = make_decision_with_gemini(parsed_query, top_chunks)
    decision_cleaned = decision_raw.strip().removeprefix("```json").removesuffix("```").strip()

    try:
        decision_data = json.loads(decision_cleaned)
    except:
        decision_data = {"error": "Failed to parse decision", "raw": decision_raw}
    


# ✅ Translate decision + justification into Marathi
    try:
        if "decision" in decision_data or "justification" in decision_data:
            english_text = (
                f"Decision: {decision_data.get('decision', '')}\n"
                f"Amount: {decision_data.get('amount', '')}\n"
                f"Justification: {decision_data.get('justification', '')}"
            )
            marathi_translation = GoogleTranslator(source='auto', target='mr').translate(english_text)
            decision_data["translation"] = {
                "english": english_text,
                "marathi": marathi_translation
            }
    except Exception as e:
        decision_data["translation_error"] = str(e)

    # Step 3: Store in MongoDB
    collection.insert_one({
        "query": query,
        "parsed_query": parsed_query,
        "decision": decision_data,
        "pdf_name": pdf_file.filename
    })

    return jsonify(decision_data)

if __name__ == "__main__":
    app.run(debug=True)
