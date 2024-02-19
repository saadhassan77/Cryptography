# Importing necessary libraries
from pwn import *

# Length of the key and maximum chunk size for sending data
KEY_LEN = 50000
MAX_CHUNK = 1000

# Connecting to the remote server
r = remote("mercury.picoctf.net", 20266)

# Receiving the encrypted flag from the server
r.recvuntil("This is the encrypted flag!\n")
flag = r.recvlineS(keepends = False)
log.info(f"Flag: {flag}")

# Converting the flag from hexadecimal to binary format
bin_flag = unhex(flag)

# Calculating the remaining bytes needed to reach the desired key length
counter = KEY_LEN - len(bin_flag)

# Sending chunks of data to cause wrap-around until reaching the desired key length
with log.progress('Causing wrap-around') as p:
    while counter > 0:
        p.status(f"{counter} bytes left")
        chunk_size = min(MAX_CHUNK, counter)
        r.sendlineafter("What data would you like to encrypt? ", "a" * chunk_size)
        counter -= chunk_size

# Sending the original binary flag to the server for decryption
r.sendlineafter("What data would you like to encrypt? ", bin_flag)

# Receiving and printing the decrypted flag
r.recvlineS()
log.success("The flag: {}".format(unhex(r.recvlineS())))

