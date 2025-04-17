from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from utils.extract import extract_phrases  # Importing extract function
from utils.process import process_document  # Importing process function

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET"])
def home():
    return "✅ Plagiarism Checker API is running", 200

# Upload file route
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"message": "No file part in the request"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"message": "No file selected"}), 400

    try:
        # Save the uploaded file to disk
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200
    except Exception as e:
        return jsonify({"message": f"Failed to save file: {str(e)}"}), 500


# Plagiarism check route
@app.route("/check-plagiarism", methods=["POST"])
def check_plagiarism():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    try:
        # Save the file to disk
        file.save(file_path)

        # Step 1: Extract phrases from the uploaded file
        phrases = extract_phrases(file_path)
        
        # Step 2: Process the document by scraping and comparing similarity
        result = process_document(file_path)

        return jsonify({
            "message": "Plagiarism check completed",
            "file": file_path,
            "matches": result['matches'],
            "total_phrases": result['total_phrases'],
            "matched_count": result['matched_count']
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))