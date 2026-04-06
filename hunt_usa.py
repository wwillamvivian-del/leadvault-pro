import requests
import time

GITHUB_TOKEN = "ghp_9MBD3RqoqX97oRf6muuJBT1bDLdPAK3Z9l2o"

def master_hunt():
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    # This URL is optimized to find people with GMAIL in their profile
    url = "https://api.github.com/search/users?q=gmail+location:USA&per_page=50"
    
    print("--- Target: Gmail Users in USA... ---")
    found = 0
    
    try:
        r = requests.get(url, headers=headers)
        users = r.json().get('items', [])
        
        with open("usa_5.txt", "w") as f:
            for u in users:
                if found >= 5: break
                
                profile = requests.get(u['url'], headers=headers).json()
                email = profile.get('email')

                # Check if they have a real gmail address visible
                if email and "gmail.com" in email:
                    found += 1
                    f.write(f"EMAIL: {email}\n")
                    print(f"[{found}] SUCCESS: {email}")
                
                time.sleep(1)
                
        print(f"\n--- DONE! Found {found} leads. ---")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    master_hunt()
