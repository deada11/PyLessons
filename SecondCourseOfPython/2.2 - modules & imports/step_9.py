import simplecrypt

with open('encrypted.bin', 'rb') as inp:
    encrypted = inp.read()

with open('passwords.txt', 'r') as passwords:
    pwd = passwords.read().splitlines()

for key in pwd:
    try:
        print(simplecrypt.decrypt(key, encrypted).decode('utf8'))
    except simplecrypt.DecryptionException:
        print(key, 'is wrong')
    else:
        print(key, 'is correct')
        break
