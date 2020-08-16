# ввод строк
incomingString = input()
outcomingString = input()
forEncryprt = input()
forDecrypt = input()

# создание списков значений и словаря ключ-шифр
key = [i for i in incomingString]
cypher = [i for i in outcomingString]
encrypt = [i for i in forEncryprt]
decrypt = [i for i in forDecrypt]
decryptionDict = dict(zip(key,cypher))

encrypted = []
for i in encrypt:
    encrypted.append(decryptionDict[i])

decryptionDict = dict(zip(decryptionDict.values(),decryptionDict.keys()))
decrypted = []
for i in decrypt:
    decrypted.append(decryptionDict[i])

# вывод зашифрованных строк
print(''.join(encrypted))
print(''.join(decrypted))