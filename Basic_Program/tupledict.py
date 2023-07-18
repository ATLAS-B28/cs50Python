'''
test_dict = {'month': [1, 2, 3],
             'name': ['Jan', 'Feb', 'March']}
result = {test_dict["month"][i]:test_dict["name"][i] for i in range(len(test_dict['month']))}
print(result)

list = [{"name": "Aditya", "age": 20},
       {"name": "ABC", "age": 20},
       {"name": "A123", "age": 19}]

print(sorted(list,key=lambda i : (i['age'],i['name'])))

import operator

def counting_frequency(my_list):
    freq = {}
    for items in my_list:
        freq[items] = my_list.count(items)

    for key,value in freq.items():
             print("% d : % d" % (key, value))

if __name__ == "__main__":
          my_list = [1, 1, 1,1,1,1,1,1,1,1,1,1, 5, 5,5,5,5,5,5, 3, 1, 3,3,3,3,3,3,3,3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
          counting_frequency(my_list)


def max_mim_k(test,k):
  print(f"Original tuple is: {str(test)}")

  res= [] #list
  arb = k
  test_list = list(sorted(test))

  for index,val in enumerate(test_list):
    if index < arb or index >= len(test_list) - arb:
      res.append(val)
  res = tuple(res)

  print(f"Extracted value: {str(res)}")


test_tuple = tuple(input("Enter the tuple values: "))
k = int(input("Enter the arbitatary value: "))
max_mim_k(test_tuple,k) 

def val_and_cube(my_list,a):
    res = [(val, pow(val,3)) for val in my_list]
    print(res)

list1 = [1,8,9,5,6]
i = int(input("Enter the number: "))
val_and_cube(list1,i)

test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
 
# initializing the target tuple
tup = (17, 23)
 
# initializing the index of the element to compare in each tuple
K = 1
def key_func(t):
    return abs(t[K-1] - tup[K-1])

sorted_list  =sorted(test_list,key=key_func)

result = sorted_list[0]

print(f'The nearest tuple to Kth index element is : {str(result)}')


test_tuple1 = (4, 5)
test_tuple2 = (7, 8)

print(f"The original tuple 1 :  {str(test_tuple1)}")
print(f"The original tuple 2 :  {str(test_tuple2)}")

result = [(a,b) for a in test_tuple1 for b in test_tuple2]+[(a,b) for a in test_tuple2 for b in test_tuple1]

print(f'All pair combinations of 2 tuples: {result}')


from functools import reduce

tup_list = [(15, 3), (3, 9), (1, 10), (99, 2)]
digit_list = set(reduce(lambda a,b:str(a)+str(b),tup) for tup in tup_list)
digit_list = set(digit for string in digit_list for digit in string)

print("The original list is:", tup_list)
print("The extracted digits:", digit_list)'''

