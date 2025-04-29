import requests
from bs4 import BeautifulSoup
import csv

def scrape_headlines(url="https://www.geeksforgeeks.org/"):
    try:
        print(f"Connecting to {url} ...")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = soup.find_all('h3')
        cleaned_headlines = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

        return cleaned_headlines[:10]

    except requests.RequestException as e:
        print(f"Scraping failed: {e}")
        return []

def save_to_csv(headlines, filename="scraped_data.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Headline'])
        for headline in headlines:
            writer.writerow([headline])
    print(f"Saved {len(headlines)} headlines to {filename}")

if __name__ == "__main__":
    headlines = scrape_headlines()
    if headlines:
        print("\nTop Headlines:")
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline}")
        save_to_csv(headlines)
    else:
        print("No headlines scraped.")
