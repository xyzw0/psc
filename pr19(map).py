def prime(n):
    if (n==1):
        return "np"
    elif (n==2):
        return "p"
    else:
        for x in range(2,n):
            if(n % x==0):
                return "np"''
    return "p"
l=[3,4,6,9,11]
x=map(prime,l)
print(list(x))
