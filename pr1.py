# Python Function with Arguments, and Return Value
def Addition(a, b):
    Sum = a + b
    return Sum

print("After Calling the Function:", Addition(25, 45))


# Python Function with Arguments, and NO Return Value
def Multiplications(a, b):
    Multi = a * b
    print("After Calling the Function:", Multi)
    
Multiplications(10, 20)


# Python Function with No Arguments, and with Return Value
def Multiplication():
    a = 10
    b = 25
    Multi = a * b
    return Multi
print("After Calling the Multiplication : ", Multiplication())


# Python Function with No Arguments, and No Return Value
def Adding():
    a = 20
    b = 30
    Sum = a + b
    print("After Calling :", Sum)
    
    
Adding()
