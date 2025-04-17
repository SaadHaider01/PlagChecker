from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.process import process_document
import os

app = Flask(__name__)
CORS(app)

@app.route("/check-plagiarism", methods=["POST"])
def check_plagiarism():
    if 'document' not in request.files:
        return jsonify({"error": "No document provided"}), 400

    file = request.files['document']
    filepath = os.path.join("/tmp", file.filename)  # /tmp is writable on Vercel
    file.save(filepath)

    try:
        result = process_document(filepath)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500