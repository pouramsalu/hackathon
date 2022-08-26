num=int(input("enter the number"))
j=0
while j<num:
    x=int(input("enter the number"))
    y=int(input("enter the number"))
    count=0
    a=[]
    b=0
    while x<=y:
        a.append(x)
        x+=1
    print(a)
    if x>9:
        i=0
        while i<len(a):
            b=a[i]%10
            if b==2 or b==3 or b==9:
                count+=1
            i+=1
    else:
        i=0
        while i<len(a):
            if a[i]==2 or a[i]==3 or a[i]==9:
                count+=1
            i+=1
    print(count)