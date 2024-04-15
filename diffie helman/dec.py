from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
import hashlib
from secret import shared_secret

ciphertext_data = {'iv': '96a7f5c23a3344689b465a821ea0cf39', 'encrypted_flag': '07ba868266c6c1f0a5600d8fafd984169222d32bdb786f03f06c327c02651be2a975cbaa20e8f89f17ce9ca2579a1a74'}

def decrypt_flag(shared_secret: int, ciphertext_data: dict):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    iv = bytes.fromhex(ciphertext_data['iv'])
    ciphertext = bytes.fromhex(ciphertext_data['encrypted_flag'])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)
    unpadded_data = unpad(decrypted_data, 16)
    return unpadded_data

decrypted_flag = decrypt_flag(shared_secret, ciphertext_data)
print("Decrypted Flag:", decrypted_flag.decode('utf-8'))
