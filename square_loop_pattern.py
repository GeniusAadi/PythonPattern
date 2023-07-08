a = int(input("num= "))
for i in range(a,0,-1):
    for j in range(a,0,-1):
        if j > i:
            print(j,end="")
        else:
            print(i,end="")
    for k in range(2,a+1):
        if k > i:
            print(k,end="")
        else:
            print(i,end="")
    print()
for l in range(2,a+1):
    for m in range(a,1,-1):
        if m >= l:
            print(m,end="")
        else:
            print(l,end="")
    for n in range(2,a+1):
        if n == l:
            print(n,end="")
    for o in range(2,a+1):
        if o >= l:
            print(o,end="")
        else:
            print(l,end="")
            #print()
    print()