#kite of numbers
a = 1
for i in range(1,4):
    for j in range(4,i,-1):
        print(" ",end="")
    for k in range(1,a+a,1):
        print(k,end="")
    a+=1
    print()
