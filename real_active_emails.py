import requests
import random
import string
import json
import time

def generate_active_emails(count=50):
    # Professional subjects to avoid "(no subject)"
    subject_list = [
        "Welcome to the Team", "Project Update", "Invoice #2024-01",
        "Meeting Request", "Security Verification Code", "Your Subscription"
    ]
    
    # Get a valid domain
    domain_resp = requests.get("https://api.mail.tm/domains")
    domain = domain_resp.json()['hydra:member'][0]['domain']
    
    print(f"Generating {count} active emails with subjects...")

    for i in range(count):
        user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        address = f"{user}@{domain}"
        password = "Password123!"
        chosen_subject = random.choice(subject_list)
        
        # Register the account
        data = {"address": address, "password": password}
        headers = {'Content-Type': 'application/json'}
        resp = requests.post("https://api.mail.tm/accounts", data=json.dumps(data), headers=headers)
        
        if resp.status_code == 201:
            # Save the email, password, and its subject to a file
            with open('active_citizens.txt', 'a') as f:
                f.write(f"EMAIL: {address} | PWD: {password} | SUBJECT: {chosen_subject}\n")
            print(f"[{i+1}] SUCCESS: {address} | Subject: {chosen_subject}")
        else:
            print(f"[{i+1}] Rate limit hit. Waiting...")
            time.sleep(5)
            
        time.sleep(1) # Small delay to keep the server happy

    print("\n--- DONE! All records saved to 'active_citizens.txt' ---")

if __name__ == "__main__":
    generate_active_emails(50)
