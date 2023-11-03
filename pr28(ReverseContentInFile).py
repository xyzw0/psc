# Create a file
fname = input("Enter file name: ") #reverse.txt
# Enter data in file
fopen=open(fname,'w')
fopen.write(" World \n Hello ")
fopen.close()

# Read the file in Reverse Order
for line in reversed(list(open(fname))):
    print(line.rstrip())
