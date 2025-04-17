import requests
from bs4 import BeautifulSoup
import json
import time
import urllib.parse

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

def scrape_google_results(phrases, max_results=5):
    result_map = {}

    for phrase in phrases:
        query = urllib.parse.quote_plus(phrase)
        url = f"https://html.duckduckgo.com/html/?q={query}"
        
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            results = []
            for link in soup.find_all('a', {'class': 'result__a'}, limit=max_results):
                href = link.get('href')
                if href and href.startswith('http'):
                    results.append(href)

            result_map[phrase] = results

            # Avoid getting blocked
            time.sleep(2)

        except Exception as e:
            print(f"Error scraping for phrase '{phrase}':", e)
            result_map[phrase] = []

    # Save results to JSON file
    try:
        with open('backend/utils/scraped_results.json', 'w', encoding='utf-8') as f:
            json.dump(result_map, f, indent=4)
        print("Scraped results saved to scraped_results.json")
    except Exception as e:
        print("Error saving scraped results:", e)

    return result_map

# Example usage for testing:
# if __name__ == "__main__":
#     phrases = ["quantum computing applications", "neural networks in AI"]
#     scrape_google_results(phrases)
