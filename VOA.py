b = 8
for i in range(1,5):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,b):
        print(k,end="")
    b=b-2
    print()
a = 4
for l in range(1,4):
    for m in range(4,l+1,-1):
        print(" ",end ="")
    for n in range(1,a):
        print(n,end="")
    a = a +2
    print()
