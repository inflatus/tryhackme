### Intro

never use --force can generate false positives

crack the hash d0199f51d2728db6011945145a1b607a with a rainbow table

found out it is an MD5 hash

hashcat -m 0 -a 0 hashes /usr/share/wordlists/rockyou.txt

basketball

### Cracking the Hash

crack the hash 5b31f93c09ad1d065c0491b764d04933 with online tools

tryhackme

seems this was supposed to be online because it is not in a rainbow table (which I verified with the rockyou.txt)

### Note

should not encrypt passwords

### Rounds

How many rounds does sha512crypt ($6$) use by default?

5000 if you do not use the rounds option this is the default

### Example Hash Citrix Netscaler

asking about Citrix NetScaler example hash

8100  Citrix NetScaler  1765058016a22f1b4e076dccd1c3df4e8e5c0839ccded98ea

### hash Length

how long is ntlm hash

1000  NTLM  b4b9b02e6f09a9bd760f388b67351e2b

32

### Crack Hash Bcrypt

crack the hash $2a$06$7yoU3Ng8dHTXphAg913cyO6Bjs3K5lBnwq5FJyA6d01pMSrddr1ZG

bcrypt

### Crack Hash SHA-256

crack the hash 9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1

sha-256

halloween
