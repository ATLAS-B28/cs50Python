#print("hello world")
#take input
#print("Type in the name of candidate: ")
#name = input("Name : ")
#print("Name of the candidate is : "+ name)
#conditions
#n = int(input("Number: " ))
#if n > 0:
#    print("n is positive")
#else :
 #   print("n is negative")
#sequence
#name = "aditya"
#print(name[0])#get the 1st item of the string
#tuple sequence of immutable values
#coordinates = (17.8,23.4)
#list sequnce of mutable values 
#name_list = ["aditya","kakashi","naruto"]
  #we can add ,remove 
#name_list.append("akatsuki") #appends at the end
#print(name_list)
#name_list.sort() # here sorts aplhabetically
#print(name_list)
#set collection of unique values
#s = set()
 #add elements
#s.add(1)
#s.add(2)
#s.add(3)
#s.add(4)
#s.add(4)#this is repeated and therefore appears only once
#s.remove(2)
#print(f"The set has {len(s)} elements.")
#dict collection of key-value pairs
#d = {1:"Aditya",2:"Kakashi"}
#d[3] = "Naruto"
#print(d)
#loop
#for a in range(6):
#    print(a)

#name_list = ["aditya","kakashi","naruto"]

#for name in name_list :
#    print(name)

#functions
#def square(x):
#    return x * x

#from Functions import square
import Functions 
for i in range(10):
    #print(f"The sqarre of{i} is {square(i)}.")
    print(f"The sqarre of{i} is {Functions.square(i)}.")
