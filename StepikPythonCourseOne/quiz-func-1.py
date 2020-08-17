
def DecToBin (dec):
    arr = ''
    while dec > 0:
        dec, arr = dec // 2, str (dec % 2) + arr
    print (arr)

DecToBin(int(input()))