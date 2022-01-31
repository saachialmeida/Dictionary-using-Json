import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
        yn= input("Did you mean %s instead? Enter y if yes and n if no: " % get_close_matches(w,data.keys())[0])
        if yn=="y":
            return  data[get_close_matches(w,data.keys())[0]]
        elif yn=="n":
            return "This word does not exist.Please double check."
        else:
            return "Your entry isnt matching with the given options.Please try again."
    else:
        return "The word does not exist.Please try again"
word=input("Enter Word: ")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)