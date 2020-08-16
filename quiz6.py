dec = int(input())
bina=''
while dec > 0:
    dec, bina = dec // 2, str(dec%2) + bina
print(bina)