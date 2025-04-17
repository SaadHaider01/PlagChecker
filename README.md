# 📄 Plagiarism Checker

An intelligent plagiarism checker that allows users to upload `.pdf`, `.docx`, or `.txt` files, extracts random phrases, performs online searches, scrapes top search results, and calculates a similarity score to detect possible plagiarism.

---

## 🚀 Features

- Upload support for `.pdf`, `.docx`, and `.txt` files
- Intelligent random phrase extraction (5–10 words each)
- Real-time search using DuckDuckGo for extracted phrases
- Web scraping of top search results
- Text similarity analysis using token matching
- Clean UI with file preview and toast notifications
- Returns matched phrases, source URLs, and a similarity percentage
- Option to generate a PDF report (optional for future scaling)

---

## 🗂️ Project Structure

```
backend/
│
├── app.py                    # Flask app entry (optional)
├── server.py                 # Main Flask server with endpoints
├── requirements.txt          # Python dependencies
├── test_document.txt         # Sample test file
├── uploads/                  # Uploaded files go here
│   └── pcafinal.pdf
└── utils/
    ├── extract.py            # Phrase extraction logic
    ├── phrases.json          # Saved extracted phrases
    ├── process.py            # Core processing pipeline
    ├── scraper.py            # Web scraping logic
    └── similarity.py         # Similarity comparison logic
```

---

## 🛠️ Installation

### ⚙️ Backend (Python + Flask)

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/plagiarism-checker.git
cd plagiarism-checker/backend
```

2. **Create a virtual environment and activate it:**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the server:**

```bash
python server.py
```

By default, the Flask server runs at `http://localhost:5000`.

---

## 📤 API Endpoints

### `POST /upload`

- **Description**: Upload a document to check for plagiarism.
- **Request**: Multipart/form-data with file field.
- **Response**:
```json
{
  "matches": [
    {
      "phrase": "quantum computing applications",
      "sources": [
        "https://example.com/1",
        "https://example.com/2"
      ]
    }
  ],
  "total_phrases": 10,
  "matched_count": 4
}
```

---

## 💻 Frontend

- Frontend built with **React + TailwindCSS + Sonner** for toasts
- Allows file uploads and previews
- Displays loading spinner while checking
- Shows match results and plagiarism percentage

> ⚠️ Make sure to update the frontend API URL to your deployed backend when going live.

---

## 🚧 To-Do

- [ ] Background task processing (Celery, RQ)
- [ ] PDF report generation
- [ ] User authentication
- [ ] Database integration for saved reports
- [ ] Rate limiting to prevent abuse

---

## 🌐 Deployment Guide

1. **Backend**:
   - Use Heroku, Railway, or AWS to deploy Flask
   - Use Gunicorn for production:
     ```bash
     gunicorn server:app
     ```
   - Configure `CORS`, static files, and file uploads

2. **Frontend**:
   - Use Vercel, Netlify, or GitHub Pages to deploy React
   - Update environment variables for production API URLs

3. **Domain + SSL**:
   - Use Namecheap, GoDaddy, etc.
   - Platforms like Heroku/Vercel handle HTTPS automatically

---

## 📌 Tech Stack

- **Frontend**: React, Tailwind CSS, Sonner
- **Backend**: Flask, BeautifulSoup, PyPDF2, python-docx, requests
- **Web Scraping**: DuckDuckGo HTML Search
- **Similarity Logic**: Custom phrase-token matching
- **Deployment**: Heroku / Vercel / Railway

---

## 🙌 Acknowledgements

Special thanks to:

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [DuckDuckGo](https://duckduckgo.com/)
- [Flask](https://flask.palletsprojects.com/)

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use, modify, and share!

---

## ✉️ Contact

For queries or collaboration:
- Email: [saadhaider349@gmail.com]
- GitHub: [https://github.com/SaadHaider01]
