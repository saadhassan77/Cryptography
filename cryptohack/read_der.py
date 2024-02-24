from Crypto.PublicKey import RSA

f = open('2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der','rb')
a = RSA.importKey(f.read())
print(a.n)
