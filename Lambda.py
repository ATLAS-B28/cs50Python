#lambda - an nameless function 
name = [
    {"name":"Aditya","village":"Amegakure"},#<-dict
    {"name":"Kakashi","village":"Konohagakure"},
    {"name":"Gaara","village":"Sunagakure"},
    {"name":"Neji","village":"Konohagakure"},
]#<-list

#def sorted(person):
    #return person["name"]#<-acts a key
 #   return person["village"]#<-acts a key

#lambda function form
#name.sort(key=sorted)
name.sort(key=lambda person: person["name"])
print(name)