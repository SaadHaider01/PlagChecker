from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from utils.process import process_document  # ✅ full pipeline logic here

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return "✅ Plagiarism Checker Backend Running"

@app.route('/test', methods=['GET'])
def test_route():
    return "Test route is working!"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return jsonify({'message': 'File uploaded successfully', 'filename': file.filename}), 200

def process_document(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    return {'message': 'Plagiarism check completed successfully', 'content': content}

@app.route('/check-plagiarism', methods=['POST'])
def check_plagiarism():
    print("Plagiarism check initiated")

    if 'document' not in request.files:
        return jsonify({'error': 'No document provided'}), 400

    file = request.files['document']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        result = process_document(filepath)  # ✅ Full end-to-end logic
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
