def expand(l):
    a=[]
    for i in range(1,l+1):
        n=int(input(" Enter here: "))
        a.append(n)
    print("first list:",a)
    b=[]
    for i in range(1,len(a)):
        d=abs(a[i]-a[i-1])
        b.append(d)
    print("new list:",b)
    c=True
    for i in range(1,len(b)):
        if b[i]<=b[i-1]:
            c=False
    return c
    
l=int(input("number of elements in list: "))
print(expand(l))
