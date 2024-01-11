import requests
import json
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

#generate a key pair for the user
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

user_name = "John Doe"
user_email = "john.doe@example.com"

#create a claim with the user's identity information
claim = {'username':user_name, 'user_email':user_email}

#sign the claim with the user's private key
claim_json = json.dumps(claim)
signature = private_key.sign(
    claim_json.encode('utf-8'),
    padding.PSS(
        mgf = padding.MGF1(hashes.SHA256()),
        salt_length = padding.PSS.MAX_LENGTH

    ),
    hashes.SHA256()
)

# Include the signed claim in the request to the server
signature_base64 = base64.b64encode(signature).decode('utf-8')
data = {'signed_claim': {'user_name': user_name, 'user_email': user_email, 'signature': signature_base64()}}
response = requests.post('http://localhost:5001/verify', json=data)

# Process the server's response
if response.status_code == 200:
    result = response.json()
    if result['result'] == 'success':
        print(f"Server verification successful. Identity: {result['identity']}")
    else:
        print(f"Server verification failed. Message: {result['message']}")
else:
    print(f"Error communicating with the server. Status code: {response.status_code}")

