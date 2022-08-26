x=int(input("enter the number"))
y=int(input("enter the number"))
def num(x,y):
    if x<y:
        print("bike is faster")
    elif x>y:
        print("car is faster")
    elif x==y:
        print("both are same")
num(x,y)