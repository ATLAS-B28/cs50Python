import sys
try:
 x = int(input("x :"))
 y = int(input("y :"))
except ValueError:
   print("Please enter a number .")
   sys.exit(1)#helps avoid further 
              # execution and errors in the code
   
try:
    result = int(x/y)
except ZeroDivisionError:
    print(f"Error: cannot divide {x} by {y}")
    sys.exit(1)
print(result)