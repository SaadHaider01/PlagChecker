import json
from difflib import SequenceMatcher

def calculate_similarity(original_phrases, scraped_contents):
    matched = []
    for phrase in original_phrases:
        for url, content in scraped_contents.items():
            similarity = SequenceMatcher(None, phrase.lower(), content.lower()).ratio()
            if similarity > 0.8:  # 80% match threshold
                matched.append({
                    "phrase": phrase,
                    "match": content,
                    "url": url,
                    "similarity": round(similarity * 100, 2)
                })
    return matched

# Test the script
def test_similarity():
    # Load phrases from phrases.json
    with open("phrases.json", "r", encoding="utf-8") as f:
        original_phrases = json.load(f)

    # Sample scraped contents
    scraped_contents = {
        "https://example.com/page1": "This is a sample document. It contains several sentences.",
        "https://example.com/page2": "The goal is to test the functionality of phrase extraction and matching.",
        "https://example.com/page3": "Random phrases are extracted from the document, including testing phrases."
    }

    # Calculate similarity
    matched = calculate_similarity(original_phrases, scraped_contents)
    
    # Print the results
    if matched:
        for match in matched:
            print(f"Phrase: {match['phrase']}")
            print(f"Matched content: {match['match']}")
            print(f"URL: {match['url']}")
            print(f"Similarity: {match['similarity']}%\n")
    else:
        print("No matches found.")

# Run the test
test_similarity()
