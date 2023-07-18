import re
'''from collections import Counter

def most_occur_ele(word):
    arr = re.findall(r'[0-9]+',word)
    maxm = 0
    max_ele = 0
    c = Counter(arr)
    for x in list(c.keys()):
        if c[x]>=maxm:
            maxm = c[x]
            max_ele = int(x)

    return max_ele

if __name__ == "__main__":
    word = 'geek55of55gee4ksabc3dr2x'
    print(most_occur_ele(word))

def check_password(password):
    if len(password)<10:
        return False
    
    if not any(char.isupper() for char in password):
        return False
    
    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    speacial_char = "!@#$%^&*()-_=+[]{};:,.<>/?"
    if not any(char in speacial_char for char in password):
        return False

    return True 


password = str(input("Enter the password: "))
validaity = check_password(password)
if validaity:
    print("Password is valid!")
else:
    print("Password is not valid!")

regex = '[a-zA-z0-9]$'

def accept_alpha(string):
    if(re.search(regex,string)):
        print("Accept")
    else:
        print("Discard")


if __name__ == "__main__":
    string = "aditya@"
    accept_alpha(string)
    string = "aditya29"
    accept_alpha(string)'''

import re
s = "http://www.example.com/index.html"

obj1 = re.findall('(\w+)://([\w\-\.]+)/(\w+).(\w+)',s)

print(obj1)

def remove_duplicate(input):
    regex = r'\b(\w+)\W+\1\b'

    return re.sub(regex, r'\1' , input ,flags=re.IGNORECASE)

str1 = "Good bye bye world world"
print(remove_duplicate(str1))