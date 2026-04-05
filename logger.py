file_name = "my_secrets.txt"

print("--- Logger is Online ---")
print("Type a message. Type 'STOP' to exit.")

while True:
    msg = input("> ")
    if msg.upper() == "STOP":
        break
    
    # "a" means APPEND (it adds to the list instead of deleting)
    with open(file_name, "a") as f:
        f.write(msg + "\n")

print("Safe and sound. Logger closed.")
