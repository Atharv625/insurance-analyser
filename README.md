# insurance-analyser

🧾 Insurance Policy Analyzer using Gemini AI

An AI-powered Insurance Policy Analyzer that reads and interprets insurance policy PDFs, analyzes claim requests, and gives a structured decision — Approved or Rejected — along with clause-based justifications.

This project combines Flask, MongoDB, FAISS, Sentence Transformers, and Google Gemini AI to build an intelligent backend that understands both natural language and legal text.

🧠 Features

✅ Extracts text from uploaded policy PDFs using pdfplumber
✅ Breaks content into chunks and embeds them with Sentence Transformers
✅ Uses FAISS for semantic clause retrieval
✅ Employs Gemini 1.5 Flash for:

Parsing structured claim data (age, gender, procedure, etc.)

Making claim approval/rejection decisions with clear reasoning
✅ Stores all analysis results in MongoDB
✅ Simple web interface (HTML + JS + Flask backend)

🏗️ Project Structure
insurance-analyzer/
│
├── app.py # Flask backend
├── analyzer.py # AI & NLP logic (Gemini + FAISS)
├── db.py # MongoDB connection
├── templates/
│ └── index.html # Web frontend (upload & query form)
├── static/
│ └── style.css # Optional styling
├── uploads/ # Uploaded PDFs
└── README.md

⚙️ Setup Instructions
1️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate # Windows

2️⃣ Install Dependencies
pip install flask pymongo pdfplumber sentence-transformers faiss-cpu numpy google-generativeai python-dotenv

3️⃣ Set Up MongoDB

Use local MongoDB:

# db.py

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["insurance_analyzer"]
collection = db["claim_decisions"]

Verify:

mongosh
use insurance_analyzer
show collections

4️⃣ Run the Flask App
python app.py

Open → http://127.0.0.1:5000

🧩 Workflow

Upload an insurance policy PDF.

Enter a natural language claim query (e.g., "Patient requests knee surgery claim")

Backend extracts PDF text → chunks → embeddings → top relevant clauses.

Gemini AI parses query details and evaluates eligibility.

Final structured output is returned as JSON and stored in MongoDB.

🧰 Tech Stack
Layer Tools Used
Frontend HTML, JavaScript
Backend Flask
AI/NLP Sentence Transformers, FAISS, Gemini 1.5 Flash
Database MongoDB (Local)
PDF Parsing pdfplumber
📊 Example Output
{
"decision": "rejected",
"amount": "Not applicable",
"justification": "The submitted claim details for 'knee surgery' ...",
"referenced_clauses": [
"Illness / towards expenses incurred Disease ...",
"Hospitalization • Attending Surgeon’s Prescription ..."
]
}

🧠 Future Enhancements

Add user authentication for claim history

Support multiple policy formats (image, scanned PDFs)

Integrate Gemini 2.0 or fine-tuned models for domain accuracy

Create dashboard visualization for analytics

👨‍💻 Author

Atharv Patil
Department of Information technology
