import os
import json
from utils.extract import extract_phrases
from utils.scraper import scrape_google_results
from utils.similarity import calculate_similarity

def process_document(file_path):
    # 1. Extract phrases from the uploaded document
    phrases = extract_phrases(file_path)

    # 2. Save phrases to file
    phrases_path = os.path.join("D:/prag-check/backend/utils", "phrases.json")
    with open(phrases_path, 'w', encoding='utf-8') as f:
        json.dump(phrases, f, indent=4)

    print(f"[✔] Extracted {len(phrases)} phrases")

    # 3. Scrape Google search results for those phrases
    scraped_results = scrape_google_results(phrases)

    # 4. Save scraped results
    scraped_path = os.path.join("D:/prag-check/backend/utils", "scraped_results.json")
    with open(scraped_path, 'w', encoding='utf-8') as f:
        json.dump(scraped_results, f, indent=4)

    print(f"[✔] Scraped search results for {len(scraped_results)} phrases")

    # 5. Calculate similarity between phrases and scraped data
    matched_phrases = calculate_similarity(phrases, scraped_results)

    print(f"[✔] Found {len(matched_phrases)} potentially plagiarized phrases")

    return {
        "matches": matched_phrases,
        "total_phrases": len(phrases),
        "matched_count": len(matched_phrases)
    }

# Optional usage example
# result = process_document("backend/test_document.txt")
# print(result)
