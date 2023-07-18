'''string  = "Aditya Bhambere is from Bharat"
def reverse_string(string):
 stack = []
 
 for s in string:
   stack.append(s)

 reverse = []
 while stack:
   reverse.append(stack.pop())

 reverse_result = ''.join(reverse)

 print(reverse_result)

reverse_string(string)

def remove_letter(text_letter,a):
   text_len = len(text_letter)
   new_str = ''
   for i in range(text_len):
     if i != a:
       new_str = new_str + text_letter[i]
    
   return new_str

input_str = str(input("Enter the String: "))
input_pos = int(input("Enter the Letter: "))

print(f'Result :{ remove_letter(input_str,input_pos)}')



def count_same_words(str1,str2):
    str_set_1 = set(str1)
    str_set_2 = set(str2)
    matched_elements = str_set_1 & str_set_2
    print(f'No.of matching letters: {str(len(matched_elements))}')

input1 = str(input("Enter 1st string: "))
input2 = str(input("Enter 2nd string: "))

count_same_words(input1,input2)

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
'''
def val_and_cube(my_list,a):
    res = [(val, pow(val,3)) for val in my_list]
    print(res)

list1 = [1,8,9,5,6]
i = int(input("Enter the number: "))
val_and_cube(list1,i)


