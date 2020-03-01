file = open("fruits.txt",'r')
content = file.readlines()
# for i in content:
#     print(len(i))
file.close()
for i in content:
    print(len(i.strip()))