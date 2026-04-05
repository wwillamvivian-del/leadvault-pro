        # This generates a real city/state/zip combination
        location = fake.location_on_land() 
        
        citizen = {
            'Name': f"{first_name} {last_name}",
            'Email': f"{user_name}@{random.choice(trusted_domains)}",
            'Phone': fake.phone_number(),
            # We use a real-looking house number + a common street name
            'Address': f"{random.randint(100, 9999)} Main St", 
            'City': fake.city(),
            'State': fake.state(),
            'ZipCode': fake.postcode(),
            'BirthDate': fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d'),
            'SSN': fake.ssn()
        }
