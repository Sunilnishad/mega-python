# def celsius_to_feh(c):
#     return c*(9/5) + 32
# value = float(input("Enter the celsius :"))
# if value <= -273.15:
#     print("Temperature is less than -273.15C")
# else:
#     print("Fehrenheit is ", celsius_to_feh(value), " degree")
#

temp = [10,-20,-289,100]
def celsius_to_feh(c):
    if c<= -273.15:
        file.write("Temperature prediction is wrong")
    else:
        f = c*9/5 + 32
        return f
file = open("temp.txt",'w')
for i in temp:
    file.write(str(celsius_to_feh(i))+"\n")
file.close()

