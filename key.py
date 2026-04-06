import sys

# The file where "keystrokes" are stored
log_file = ".secret_log.txt"

print("--- Educational Logger Active ---")
print("Everything typed here is being recorded.")
print("Type 'EXIT' to stop and view the log.")

try:
    while True:
        # This acts as our input listener
        data = input("> ")
        
        if data == "EXIT":
            break
            
        with open(log_file, "a") as f:
            f.write(data + "\n")
            
except KeyboardInterrupt:
    pass

print(f"\nLogger stopped. Results saved to {log_file}")
