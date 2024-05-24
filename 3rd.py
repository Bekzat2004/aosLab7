import rsa
(public_key, private_key) = rsa.newkeys(512)
def encrypt_message(message, pub_key):
 return rsa.encrypt(message.encode(), pub_key)
def decrypt_message(encrypted_message, priv_key):
 return rsa.decrypt(encrypted_message, priv_key).decode()
message = "Advanced Operating Systems"
encrypted_message = encrypt_message(message, public_key)
print(f"Encrypted message: {encrypted_message}")
decrypted_message = decrypt_message(encrypted_message, private_key)
print(f"Decrypted message: {decrypted_message}")
