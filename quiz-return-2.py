def BinToDec(arr2):
    dec = 0
    for i in range (1, len(arr2)+1):
        dec += int(arr2[-i])*(2**(i-1))
    print(dec)

BinToDec(input())