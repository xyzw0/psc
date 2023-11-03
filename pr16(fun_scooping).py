x = 15
def fun():
    global x
    x = 20
    
fun()
print("Function Scoping :", x)
