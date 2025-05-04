import secrets

# Generate a 32-character (16 bytes) hexadecimal secret key
secret_key = secrets.token_hex(16)
print("Your secret key is:", secret_key)
print("\nCopy this key and paste it in your .env file as SECRET_KEY=") 