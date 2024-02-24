from Crypto.Util.number import long_to_bytes

# Given integer
given_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert integer to bytes
message_bytes = long_to_bytes(given_integer)

# Decode bytes to obtain the message
message = message_bytes.decode('ascii')

print("Message:", message)
