#I) without recursion
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*n
        n-=1
    print("The factorial is: ",f)
fact(5)


#II) with recursion
def fact(n):
    if n == 1:
        return 1
    else:
        return n*(fact(n-1))
fact(5)