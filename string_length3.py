def string_length(s):
    return len(s)
str = input("Enter the string : ")
if str in "Sunil":
    print("Length of a string is", string_length(str))
else:
    print("Value does not match the requirement!")

# def string_length(mystring):
#     if type(mystring) == int:
#         return "Sorry, integers don't have length"
#     elif type(mystring) == float:
#         return "Float is not required"
#     else:
#         return len(mystring)
# mystring =input()
# print(string_length(mystring))