dict1={}
print("1. Create Dictionary")
print("2. Update element in dictionary")
print("3. Append to dictionary")
print("4. Delete whole dictionary")
print("5. Delete particular element")
print("6. Sort the dictionary")
print("7. Find length of dictionary")
print("8. Exit")
while True:
    ch = int(input("\nEnter choice = "))
    if ch == 1:
        val=input("Enter value : ")
        key=int(input("Enter the key : "))
        dict1[key]=val
        print("Dictionary Created : ",dict1)
    elif ch == 2:
        val=input("Enter value : ")
        key=int(input("Enter the key : "))
        dict1[key]=val
        print("Updated Dictionary : ",dict1)
    elif ch == 3:
        val = input("Enter the value:")
        key = int(input("Enter the key: "))
        dict1[key] = val
        print("Appended Dictionary : ",dict1)
    elif ch == 4:
        if(dict1=={}):
            print("Dictionary is empty")
        else:
            dict1.clear()
        print("Dictionary Deleted")
        print(dict1)
    elif ch == 5:
        key = int(input("Enter the key to be popped: "))
        dict1.pop(key)
        print("Dictionary after deleting element : ", dict1)
    elif ch == 6:
        print(sorted(dict1.items()))
    elif ch == 7:
        print("The length of dictionary is:", len(dict1))
    elif ch == 8:
        print("Exit")
        break
    else:
        print("Invalid choice, Please try again")
