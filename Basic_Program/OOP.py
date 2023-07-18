#object
#class
#inheritance
#abstraction
#polymorphism
#encapsulation
#class Point():
    #automatically the init is called 
    #when an object instance is created
 
#def __init__(self,input1,input2):
        #self - indicates the current object and 
        # store the input values as the values within object
        #the 2nd and 3rd are the input values to create
        # the point 
 #    self.x = input1 
  #   self.y = input2

       

#p = Point(2,7)
#print(p.x)

#class Flight():
 #  def __init__(self,capacity):
  #    self.capacity = capacity
   #   self.passenger = []
    
  # def add_passenger(self,name):
   #   if not self.available_seats():
    #    return False
     # self.passenger.append(name)
      #return True

  # def available_seats(self):
   #   return self.capacity - len(self.passenger) 

#flight = Flight(4)
#people = ["Aditya","Kakashi","Sasuke","Minato","Jiraya"]
#for person in people:
 #  success = flight.add_passenger(person)
  # if success:
   #   print(f"Added {person} to flight successfully")
   #else:
    #  print(f"Seat not available for {person}")  

#decorators - wrappers around function or object
# to extend and add functionality on existing
# functions and objects
def decorator(func):
    def wrapper():#adding something to the hello()
        print("This is before inner function execution")
        func()#this can access the outer local variables
        print("Inner function execution complete")
    return wrapper

@decorator #add the dec decorator function to the hello()
def hello():
    print("Hello from inner function execution")

hello()#simply called the function that is wrapped again