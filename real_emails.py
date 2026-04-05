import requests
import random
import string
import json
import time

def generate_remaining_emails(target_count=38):
    print(f"Starting to generate the remaining {target_count} REAL inboxes...")
    
    # Get a valid domain
    domain_resp = requests.get("https://api.mail.tm/domains")
    domain = domain_resp.json()['hydra:member'][0]['domain']
    
    success_count = 0

    while success_count < target_count:
        # Create random credentials
        user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        address = f"{user}@{domain}"
        password = "Password123!"
        
        data = {"address": address, "password": password}
        headers = {'Content-Type': 'application/json'}
        
        try:
            resp = requests.post("https://api.mail.tm/accounts", data=json.dumps(data), headers=headers)
            
            if resp.status_code == 201:
                success_count += 1
                print(f"[{success_count}/{target_count}] CREATED: {address}")
                
                # 'a' means APPEND - it adds to your existing 12 emails
                with open('valid_inboxes.txt', 'a') as f:
                    f.write(f"{address}\n")
                
                # Wait 2 seconds before the next one
                time.sleep(2)
            
            elif resp.status_code == 429:
                print("Rate limit hit. Waiting 10 seconds to cool down...")
                time.sleep(10)
            
            else:
                print(f"Error {resp.status_code}. Retrying...")
                time.sleep(5)

        except Exception as e:
            print(f"Connection error: {e}. Retrying in 5 seconds...")
            time.sleep(5)

    print(f"\nDone! All 50 emails (12 old + 38 new) are now in 'valid_inboxes.txt'")

if __name__ == "__main__":
    generate_remaining_emails(38)
