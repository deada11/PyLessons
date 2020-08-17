a  = [ int(i) for i in input().split()]
print(len(a))
if len(a)==1:
    print(a[0])
else:
    for i in range(0,len(a)-1):
        print(a[i-1]+a[i+1],end= ' ')
    print(a[len(a)-2]+a[0])