log_file = "my_notes.txt"

print("--- Logger Started ---")
print("Type anything and hit Enter to save it.")
print("Type 'STOP' to finish.")

while True:
    entry = input("> ")
    if entry == "STOP":
        break
    
    with open(log_file, "a") as f:
        f.write(entry + "\n")
        print("Entry saved!")

print(f"Check your file by typing: cat {log_file}")
