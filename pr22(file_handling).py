#Create a file
fname = input("Enter file name: ") #file1.txt

#Enter data in file
fopen=open(fname,'w')
fopen.write("Hello World Hello")
fopen.close()

# 1st
fin = open("file1.txt","r")
str = fin.read()
l = str.split()
count_words = 0
for i in l:
    count_words = count_words + 1
print("Total Number of words : ",count_words)
fin.close()

# 2nd
with open("file1.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines : ', lines)
    
# 3rd
k = 0
word=input("Enter word to be searched : ")

with open("file1.txt", 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if (i == word):
                k = k + 1
print("Occurrences of the particular word : ", k)

# 4th
char = input("Enter character to be searched : ")
file=open("file1.txt",'r')
text=file.read()
k=text.count(char)
print("Occurrences of the particular char : ", k)

# 5th
file = open("file1.txt", "r")
count = 0
while True:
    # this will read each character and store in char
    char = file.read(1)
    if char.isspace():
        count += 1
    if not char:
        break
print("No of blankspaces in file : " , count)