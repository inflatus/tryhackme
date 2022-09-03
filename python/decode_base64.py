'''decode encodedflag.txt file'''

import base64

encoded_file = open("encodedflag.txt")

flag = encoded_file.read()

code = ""

for i in range(0, 5):
    code = base64.b16decode(flag)
    flag = code

for i in range(0, 5):
    code = base64.b32decode(flag)
    flag = code

for i in range(0, 5):
    code = base64.b64decode(flag)
    flag = code

print(flag)
