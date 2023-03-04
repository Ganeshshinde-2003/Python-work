fl = open("file.txt","r+")
li = []

while True:
    str1 = fl.readline()
    if str1!="":
        li.append(str1)
    else: 
        break;
print(li)

wordis = ""
length = 0
for line in li:
    words = line.split()
    for x in words:
        l = len(x)
        if(l >= length):
            length = l
            wordis = x

print(f"The longest word in the file is {wordis} has {length} charecters ")