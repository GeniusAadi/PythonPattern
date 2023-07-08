for r in range(6):
    i = 0
    for c in range(7):
        if (r==0 and c%3!=0)or(r==1 and c%3==0)or(r-c==2)or(r+c==8):
            i += 1
            print(i,end="  ")
        else:
            print("  ",end=" ")
    print("\n")

'''for r in range(6):
    i = 0
    for c in range(7):
        if (r==0 and c%3!=0)or(r==1 and c%3==0)or(r==2 and c%6==0)or(r==3 and c%2==0 and c%3==0)or(r==4 and c==2 and c==4)or(r==5 and c==3):
            i += 1
            print(i,end="  ")
        else:
            print("  ",end=" ")
    print("\n")'''