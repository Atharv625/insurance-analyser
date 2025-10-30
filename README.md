# 🧾 Insurance Policy Analyzer using Gemini AI

An AI-powered Insurance Policy Analyzer that reads and interprets insurance policy PDFs, analyzes claim requests, and gives a structured decision — **Approved** or **Rejected** — along with clause-based justifications.

This project combines **Flask**, **MongoDB**, **FAISS**, **Sentence Transformers**, and **Google Gemini AI** to build an intelligent backend that understands both natural language and legal text.

---

## 🧠 Features

- ✅ Extracts text from uploaded policy PDFs using `pdfplumber`
- ✅ Breaks content into chunks and embeds them with **Sentence Transformers**
- ✅ Uses **FAISS** for semantic clause retrieval
- ✅ Employs **Gemini 1.5 Flash** for:
  - Parsing structured claim data (age, gender, procedure, etc.)
  - Making claim approval/rejection decisions with clear reasoning
- ✅ Stores all analysis results in **MongoDB**
- ✅ Simple web interface (HTML + JS + Flask backend)

---

## 🏗️ Project Structure

```
insurance-analyzer/
│
├── app.py                 # Flask backend
├── analyzer.py            # AI & NLP logic (Gemini + FAISS)
├── db.py                  # MongoDB connection
├── templates/
│   └── index.html         # Web frontend (upload & query form)
├── static/
│   └── style.css          # Optional styling
├── uploads/               # Uploaded PDFs
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Mac/Linux
```

### 2️⃣ Install Dependencies

```bash
pip install flask pymongo pdfplumber sentence-transformers faiss-cpu numpy google-generativeai python-dotenv
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up MongoDB

**Using local MongoDB:**

```python
# db.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["insurance_analyzer"]
collection = db["claim_decisions"]
```

**Verify MongoDB connection:**

```bash
mongosh
use insurance_analyzer
show collections
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
MONGODB_URI=mongodb://localhost:27017/
```

### 5️⃣ Run the Flask App

```bash
python app.py
```

Open your browser and navigate to: **http://127.0.0.1:5000**

---

## 🧩 Workflow

1. **Upload** an insurance policy PDF
2. **Enter** a natural language claim query (e.g., _"Patient requests knee surgery claim"_)
3. **Backend processes:**
   - Extracts PDF text → chunks → embeddings → retrieves top relevant clauses
4. **Gemini AI** parses query details and evaluates eligibility
5. **Final structured output** is returned as JSON and stored in MongoDB

---

## 🧰 Tech Stack

| Layer           | Tools Used                                     |
| --------------- | ---------------------------------------------- |
| **Frontend**    | HTML, JavaScript                               |
| **Backend**     | Flask                                          |
| **AI/NLP**      | Sentence Transformers, FAISS, Gemini 1.5 Flash |
| **Database**    | MongoDB (Local)                                |
| **PDF Parsing** | pdfplumber                                     |

---

## 📊 Example Output

```json
{
  "decision": "rejected",
  "amount": "Not applicable",
  "justification": "The submitted claim details for 'knee surgery' do not meet the policy requirements for coverage...",
  "referenced_clauses": [
    "Illness / towards expenses incurred Disease...",
    "Hospitalization • Attending Surgeon's Prescription..."
  ]
}
```

---

## 🚀 Usage Example

**Sample Query:**

```
"45-year-old male patient underwent appendectomy surgery. Hospital bill: ₹50,000. Pre-existing condition: diabetes."
```

**Response:**

```json
{
  "decision": "approved",
  "amount": "₹45,000",
  "justification": "Claim approved based on policy Section 3.2. Pre-existing diabetes condition covered after waiting period completion.",
  "referenced_clauses": [
    "Section 3.2: Surgical Procedures Coverage",
    "Section 5.1: Pre-existing Conditions - 2 year waiting period"
  ]
}
```

---

## 🧠 Future Enhancements

- [ ] Add user authentication for claim history tracking
- [ ] Support multiple policy formats (images, scanned PDFs)
- [ ] Integrate **Gemini 2.0** or fine-tuned models for domain-specific accuracy
- [ ] Create dashboard visualization for analytics
- [ ] Add multi-language support for policy documents
- [ ] Implement batch processing for multiple claims
- [ ] Export claim reports as PDF

---

## 📝 Requirements

```txt
flask>=2.3.0
pymongo>=4.5.0
pdfplumber>=0.10.0
sentence-transformers>=2.2.0
faiss-cpu>=1.7.4
numpy>=1.24.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the Apache-2.0 license - see the LICENSE file for details.

---

## 👨‍💻 Author

**Atharv Patil**  
Department of Information Technology

---

## 📧 Contact

For questions or suggestions, feel free to reach out or open an issue in the repository.

---

## ⚠️ Disclaimer

This tool is for educational and demonstration purposes. Always consult with legal and insurance professionals for actual claim decisions. The AI-generated decisions should be reviewed by qualified personnel before any action is taken.
