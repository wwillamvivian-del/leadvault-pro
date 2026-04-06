import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def final_safe_scrape():
    url = "https://en.wikipedia.org/wiki/List_of_photovoltaics_companies"
    # This path saves the file directly to your phone's Downloads folder
    save_path = "/sdcard/Download/solar_leads.csv"
    
    print("🌍 Fetching data from Wikipedia...")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        leads = []
        for item in soup.find_all('li'):
            name = item.get_text().strip()
            if 3 < len(name) < 50 and "solar" in name.lower():
                leads.append({"Company": name})
                print(f"✅ Found: {name}")

        if leads:
            df = pd.DataFrame(leads)
            df.to_csv(save_path, index=False)
            print(f"\n🔥 SUCCESS! File saved to: {save_path}")
            print("🚀 You can now open your Downloads folder on your phone to see it!")
        else:
            print("❌ No leads found. Check your internet connection.")

    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    final_safe_scrape()
