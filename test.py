from Qubit import Qubit
from xorEncrypt import xorEncrypt


key = ""
# data = input("Enter Data: ")
result = ""

# decodes binary string
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

# encodes string to binary 
def encode_binary_string(s):
    return ''.join([bin(ord(c))[2:].rjust(8,'0') for c in s])

# binary_converted = encode_binary_string(data)
# print(f"Data: {data} Binary: {binary_converted}")
# print(decode_binary_string(binary_converted))

key = Qubit()

print(key.value)
# buff = len(binary_converted) // len(key)
# print(f"buff: {buff}")
# for i in range(buff):
#     key += key

# print(f"Key {len(key)}: {key}")
# print(f"Data {len(data)}: {data}")

# key = key[:-(len(key)-len(data))]
# print(f"Key {len(key)}: {key}")
# print(f"Data {len(data)}: {data}")

# for i in range(len(data)):
#     result = result + str(int(data[i]) ^ int(key[i]))

# print(result)