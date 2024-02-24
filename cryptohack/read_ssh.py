
from Crypto.PublicKey import RSA

f = open('bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub','rb')
a = RSA.importKey(f.read())
print(a.d) # d properties is modulus
