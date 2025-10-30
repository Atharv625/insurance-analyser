import pdfplumber
import textwrap
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


genai.configure(api_key="your Api key here")
llm_model = genai.GenerativeModel("gemini-2.5-flash")



def read_pdf(path):
    with pdfplumber.open(path) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])


def chunk_text(text, chunk_size=300):
    return textwrap.wrap(text, width=chunk_size)

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks):
    return embedding_model.encode(chunks)

def get_top_k_chunks(query, chunk_texts, chunk_vectors, k=3):
    query_vector = embedding_model.encode([query])[0]
    index = faiss.IndexFlatL2(len(query_vector))
    index.add(np.array(chunk_vectors))
    D, I = index.search(np.array([query_vector]), k)
    return [chunk_texts[i] for i in I[0]]


def parse_query_with_gemini(raw_query):
    prompt = f"""
Extract the following structured fields from this insurance query:
- Age
- Gender
- Procedure
- Location
- Policy Duration (in months)

Query: "{raw_query}"

Return valid JSON only, with keys exactly as listed.
"""
    response = llm_model.generate_content(prompt)
    return response.text


def make_decision_with_gemini(parsed_query, top_chunks):
    prompt = f"""
You are a claims processing expert.

A user has submitted a query with these structured details:
{json.dumps(parsed_query, indent=2)}

The following policy document clauses may be relevant:
---
{chr(10).join(top_chunks)}
---

Using these clauses, answer:
- Is the claim approved or rejected?
- What is the payout amount (if mentioned)?
- Which exact clause(s) justify your decision?

Return the result in the following JSON format:

{{
  "decision": "approved/rejected",
  "amount": "Rs. XXXX" or "Not applicable",
  "justification": "Explain clearly based on which clauses you made the decision",
  "referenced_clauses": ["...clause text...", "..."]
}}
"""
    response = llm_model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    print("⚙️  Analyzer ready. Run app.py to start the web app.")
