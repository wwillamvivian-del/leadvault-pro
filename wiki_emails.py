import requests
from bs4 import BeautifulSoup
import re

def get_emails_from_wiki(url):
    print(f"Searching for real contacts on: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # This looks for anything that looks like an email address
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, soup.text)
    
    if not emails:
        # If no emails are in text, look for 'Official Website' links
        print("No direct emails found. Looking for official website links...")
        links = soup.find_all('a', href=True)
        for link in links:
            if "Official website" in link.text or "Contact" in link.text:
                print(f"Found a potential contact site: {link['href']}")
    else:
        for email in set(emails):
            print(f"FOUND REAL EMAIL: {email}")

if __name__ == "__main__":
    # Example: A page about a specific organization
    target_url = "https://en.wikipedia.org/wiki/List_of_universities_in_Nigeria"
    get_emails_from_wiki(target_url)
