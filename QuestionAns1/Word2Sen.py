import json
from difflib import get_close_matches

"""
 Using the data from Json
"""
# Loading the json file in data var.
data = json.load(open("data1.json"))

def translate(w):
    w = w.lower() # converting the value input to lower case
    """
     Checking word in data,if present the give its data elif check for closest input...
    """
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn = input("Enter value is %s instead ? if yes then enter Y else N: " % get_close_matches(w,data.keys())[0])
        if yn == "Y" or yn== "y":
            return data[get_close_matches(w,data.keys())[0]] # giving first closest value
        elif yn == "N" or yn == "n":
            return "The word does not exit's"
        else:
            return "We didn't get it !"
    else:
        if w == 'exit':
           pass # it also can  be written as : return None
        else:
            return "You enter incorrect word"

word = ""
while(word != 'exit'):
    word = input("Enter the word: ")
    print(translate(word))
