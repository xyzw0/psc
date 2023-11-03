# Create a Source file
sFile = input("Enter source file name: ") #source.txt
# Enter data in file
fopen=open(sFile,'w')
fopen.write("Hello World Hello")
fopen.close()

# Create a destination file
dFile = input("Enter destination file name: ") #des.txt

fileHandle = open(sFile, "r")
texts = fileHandle.readlines()
fileHandle.close()

fileHandle = open(dFile, "w")
for s in texts:
    fileHandle.write(s)
fileHandle.close()
fileHandle=open(dFile,"r")
texts = fileHandle.readlines()
print(texts)
print("\nFile Copied Successfully!")
