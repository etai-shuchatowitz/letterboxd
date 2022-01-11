import requests
import json

def get_token(username, password):
    url = 'https://api.letterboxd.com/api/v0/auth/token'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    data = {
        'grant_type': 'password',
        'username': username,
        'password': password
    }
    salted 

    r = requests.post(url=url, headers=headers, data=data)
    print(r.json())
    return r

def get_signature(method='', url='', body=None)
    # Create the salted bytestring
    if body is None:
        body = ""
    signing_bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode(body)]
    )
    # applying an HMAC/SHA-256 transformation, using our API Secret
    signature = hmac.new(
        str.encode(self.api_secret), signing_bytestring, digestmod=hashlib.sha256
    )
    # get the string representation of the hash
    signature_string = signature.hexdigest()
    return signature_string


# def make_letterboxd_request():

token = get_token('etai.shuchatowitz@gmail.com', 'sponge4ever')
