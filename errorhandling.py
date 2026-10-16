# try/except This keeps running even if file doesn't exist
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Could not found data.txt")
    content = "default data"
print("Done!")  # Always reaches here