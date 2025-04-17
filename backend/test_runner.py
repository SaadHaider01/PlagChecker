from utils.process import process_document

# 📄 Test file path
test_file_path = "D:/prag-check/backend/uploads/pcafinal.pdf"  # or test_document.txt / .docx

# ✅ Run the full pipeline
try:
    result = process_document(test_file_path)
    print("=== Plagiarism Report ===")
    print(f"Total Phrases Checked: {result['total_phrases']}")
    print(f"Matched Count: {result['matched_count']}")
    print("\nMatched Phrases:")
    for match in result["matches"]:
        print(f"- {match['phrase']} (found in: {match['source_url']})")
except Exception as e:
    print("❌ Error during processing:", str(e))
