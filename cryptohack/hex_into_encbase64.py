import base64
# Hex-encoded flag
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
# Convert hex string to bytes
decoded_bytes = bytes.fromhex(hex_string)

# Decode bytes to obtain the flag
flag = base64.b64encode(decoded_bytes)

print("Flag:", flag)

