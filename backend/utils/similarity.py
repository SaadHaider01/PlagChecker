import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
import json
import os

def fetch_page_text(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove scripts/styles and return plain text
        for script in soup(["script", "style"]):
            script.decompose()
        return soup.get_text(separator=" ", strip=True)

    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return ""

def calculate_similarity(phrases, scraped_results, threshold=0.7, output_path="backend/utils/matched_results.json"):
    matched_data = []

    for phrase in phrases:
        urls = scraped_results.get(phrase, [])
        for url in urls:
            page_text = fetch_page_text(url)
            similarity = SequenceMatcher(None, phrase.lower(), page_text.lower()).ratio()
            if similarity >= threshold:
                matched_data.append({
                    "phrase": phrase,
                    "url": url,
                    "similarity": round(similarity, 2)
                })

    # Save matched results to JSON
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(matched_data, f, indent=4)

    print(f"Matched results saved to {output_path}")
    return matched_data

# Example test (optional for debugging)
# if __name__ == "__main__":
#     with open("backend/utils/phrases.json", "r", encoding="utf-8") as f:
#         phrases = json.load(f)
#     with open("backend/utils/scraped_results.json", "r", encoding="utf-8") as f:
#         scraped_results = json.load(f)
#     calculate_similarity(phrases, scraped_results)
