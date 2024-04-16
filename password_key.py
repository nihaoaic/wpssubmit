from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64



def encrypt(data, key):
    key = base64.b64decode(key)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_OFB, iv)
    encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size))
    encrypted_data = base64.b64encode(encrypted_data).decode()
    iv = base64.b64encode(iv).decode()
    return {"data": encrypted_data, "iv": iv}



def decrypt(data, iv, key):
    key = base64.b64decode(key)
    iv = base64.b64decode(iv)
    cipher = AES.new(key, AES.MODE_OFB, iv)
    decrypted_data = cipher.decrypt(base64.b64decode(data))
    decrypted_data = decrypted_data.decode('utf-8')
    return decrypted_data

