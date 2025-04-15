from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from backend.utils.extract import extract_phrases
from utils.scraper import scrape_google_results
from utils.similarity import calculate_similarity

app = Flask(__name__)
CORS(app)  # Allows frontend (React) to talk to backend

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return "Plagiarism Checker Backend Running"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # TODO: Call processing logic here

    return jsonify({'message': 'File uploaded successfully', 'filename': file.filename}), 200

@app.route('/check-plagiarism', methods=['POST'])
def check_plagiarism():
    file = request.files['document']
    text = file.read().decode('utf-8')  # assuming it's a .txt or .docx converted to text
    
    phrases = extract_phrases(text)
    scraped_results = scrape_google_results(phrases)
    matched_phrases = calculate_similarity(phrases, scraped_results)
    
    return jsonify({
        "matches": matched_phrases,
        "total_phrases": len(phrases),
        "matched_count": len(matched_phrases)
    })


if __name__ == '__main__':
    app.run(debug=True)
