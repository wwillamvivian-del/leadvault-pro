import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Advanced headers to mimic a mobile phone exactly
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1'
}

def scrape_leads():
    # We are switching to a different search query that is less likely to be blocked
    url = "https://www.yellowpages.com/search?search_terms=solar+contractors&geo_location_terms=Los+Angeles%2C+CA"
    
    print("🚀 Starting Stealth Search...")
    try:
        # Crucial: Random delay to mimic a human opening a browser
        wait = random.uniform(15, 25)
        print(f"⏳ Waiting {round(wait)} seconds to look human...")
        time.sleep(wait)
        
        response = requests.get(url, headers=headers, timeout=20)
        
        if response.status_code == 403:
            print("❌ Still blocked (403). YOUR VPN IS THE PROBLEM.")
            print("👉 SWITCH YOUR VPN TO A DIFFERENT CITY (e.g., New York or Chicago) AND TRY AGAIN.")
            return

        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        leads = []
        for item in soup.find_all('div', class_='result'):
            name = item.find('a', class_='business-name').text if item.find('a', class_='business-name') else "N/A"
            phone = item.find('div', class_='phones').text if item.find('div', class_='phones') else "N/A"
            leads.append({"Company": name, "Phone": phone})
            print(f"✅ Found: {name}")

        if leads:
            pd.DataFrame(leads).to_csv('solar_leads_bulk.csv', index=False)
            print(f"\n🔥 SUCCESS! {len(leads)} leads saved.")
        else:
            print("⚠️ Page loaded but no leads found. The site layout might have changed.")

    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    scrape_leads()
