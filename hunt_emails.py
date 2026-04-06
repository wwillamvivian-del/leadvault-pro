import requests
import time

def hunt_github_emails(location="Lagos", count=50):
    print(f"--- Hunting for {count} real Gmails in {location} ---")
    
    # GitHub API Search URL
    # This looks for users in your location who have a public email
    url = f"https://api.github.com/search/users?q=location:{location}+type:user&per_page={count}"
    
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Error: Could not connect to GitHub. Try again later.")
        return

    users = response.json().get('items', [])
    found_count = 0

    with open("real_people_contacts.txt", "w") as f:
        for user in users:
            user_url = user['url']
            user_data = requests.get(user_url, headers=headers).json()
            
            email = user_data.get('email')
            name = user_data.get('name') or user['login']
            
            if email and "gmail.com" in email:
                line = f"NAME: {name} | EMAIL: {email}\n"
                f.write(line)
                print(f"FOUND: {name} ({email})")
                found_count += 1
            
            # Sleep to avoid getting blocked by GitHub
            time.sleep(1)

    print(f"\n--- DONE! Found {found_count} real Gmails. Check 'real_people_contacts.txt' ---")

if __name__ == "__main__":
    hunt_github_emails("Lagos", 50)
