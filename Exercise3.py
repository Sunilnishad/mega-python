"""
writing the name of the file as the current time...
"""
import datetime

# print(datetime.datetime.now())

filepath = datetime.datetime.now()
#strftime are from :strftime.org
with open(filepath.strftime("%Y-%m-%d-%H-%M") ,'w') as file:

    file.write("Good Bye")
