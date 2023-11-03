# Arithmetic Operators
def arithmeticOps(a, b):
    sum = a + b
    return sum


# Comparison Operators

def ComparisonOps(a, b):
    compare = (a == b)
    return compare


# Logical Operators

def LogicalOps(a, b):
    log = a and b
    return log


# Assignment Operators

def AssignmentOps(a, b):
    b += a
    return b


# MAIN

print("PYTHON OPERATORS\n")
print("1. Arithmetic Operators")
print("2. Comparison Operators")
print("3. Logical Operators")
print("4. Assignment Operators ")
print("5. Exit")

while True:
    ch = int(input("\nEnter your Choice: "))
    
    if ch == 1:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        print("Result is", arithmeticOps(a, b))
    
    elif ch == 2:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        print("Result is", ComparisonOps(a, b))
    
    elif ch == 3:
        a = True
        b = False
        print("Result is", LogicalOps(a, b))
    
    elif ch == 4:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        print("Result is", AssignmentOps(a, b))
    
    elif ch == 5:
        print("Exit")
        break

    else:
        print("Please enter a valid choice")
