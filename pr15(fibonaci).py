#using recursion
def fibonacci(n):
    if(n <= 1):
       return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
    
n = int(input("Enter number of terms : "))
print("Fibonacci sequence : ")

for i in range(n):
    print(fibonacci(i))
    

#using function as an object
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms : "))
print("Fibonacci sequence : ")
    
for i in range(n):
    print(fibonacci(i))

def obj():
    return fibonacci(n)
