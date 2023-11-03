str1="Hello World"
print("Length of the string is: ",len(str1))

result = str1.replace("l", "L")
print(result)

rev=str1[::-1]
if(str1==rev):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
    
str2="Welcome"
print("Concatenation: ",str1+" "+str2)
