from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256
from Cryptodome.Random import get_random_bytes
import base64


def generate_rsa_keys():
    length = 1024
    private_key = RSA.generate(length)
    public_key = private_key.publickey()
    return private_key, public_key


def write_key_to_file(key, filename):
    with open(filename, 'wb') as file:
        file.write(key.export_key())


def read_key_from_file(filename):
    with open(filename, 'rb') as file:
        key = RSA.import_key(file.read())
    return key


def encrypt(rsa_public_key, plain_text):
    cipher = PKCS1_OAEP.new(rsa_public_key)
    cipher_text = cipher.encrypt(plain_text)
    b64_cipher = base64.b64encode(cipher_text)
    return b64_cipher


def decrypt(rsa_private_key, b64_cipher):
    decoded_ciphertext = base64.b64decode(b64_cipher)
    cipher = PKCS1_OAEP.new(rsa_private_key)
    plaintext = cipher.decrypt(decoded_ciphertext)
    return plaintext


def sign(private_key, data):
    hash_obj = SHA256.new(data)
    signer = pkcs1_15.new(private_key)
    signature = signer.sign(hash_obj)
    b64_signature = base64.b64encode(signature)
    return b64_signature


def verify(public_key, data, signature):
    hash_obj = SHA256.new(data)
    verifier = pkcs1_15.new(public_key)
    decoded_signature = base64.b64decode(signature)
    try:
        verifier.verify(hash_obj, decoded_signature)
        return True
    except (ValueError, TypeError):
        return False


# Generate RSA keys
#private_key, public_key = generate_rsa_keys()

# Write keys to files
#write_key_to_file(private_key, 'NewKeys/private2.pem')
#write_key_to_file(public_key, 'NewKeys/public2.pem')

# Read keys from files
private_key = read_key_from_file('NewKeys/private2.pem')
public_key = read_key_from_file('NewKeys/public2.pem')

# Encrypt and decrypt
text = "Hello Srikanth!"
text_bytes = text.encode('utf-8')
hash_obj = SHA256.new(text_bytes)

encrypted_text = encrypt(public_key, hash_obj.digest())
decrypted_text = decrypt(private_key, encrypted_text)

print("Original text:", text)
print("Decrypted text:", decrypted_text)

# Sign and verify
signature = sign(private_key, hash_obj.digest())
is_verified = verify(public_key, hash_obj.digest(), signature)

print("Signature:", signature)
print("Verification:", is_verified)
