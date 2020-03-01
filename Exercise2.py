"""Using multiple writing in file"""

number = [1,2,3]
file = open("Exercise2.txt",'w')
for item in number:
    file.write(str(item)+"\n")
file.close()
