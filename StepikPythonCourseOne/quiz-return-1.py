dectobin = int(input())


def DecToBin(dectobin):
    arr = ''
    while dectobin > 0:
        dectobin, arr = dectobin // 2, str(dectobin % 2) + arr
    return int(arr)

arr2 = DecToBin(dectobin)
print(arr2)

def BinToDec(arr2):
    z = len(str(arr2))
    k = str(arr2)
    j = 0
    dec = 0
    for i in range (1, z+1):
        j = int(k[-i])*(2**(i-1))
        if j != 0:
            dec = dec + j
    print(dec)

BinToDec(arr2)
