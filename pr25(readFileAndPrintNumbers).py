# Create a file
fname = input("Enter file name: ") #file3.txt
# Enter data in file
fopen=open(fname,'w')
fopen.write("Duke1234")
fopen.close()


# read in file
print("Numbers are : ")
with open(fname, 'r') as f:
    for i in f:
        for num in i:
            if(num.isdigit()):
               print(num)
