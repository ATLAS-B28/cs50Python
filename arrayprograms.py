'''def find_largest_ele(arr):
    if not arr:
        return None
    
    largest = arr[0]

    for ele in arr:
        if ele > largest:
            largest = ele
            print(f'New largerst element is: {largest}')
        else:
            print(f'Elements remain same: {largest}')

    return largest

array = [2,3,46,7,8,99,0,3,4,5,8,9,100,1000,3,0,2000]
largest_ele = find_largest_ele(array)
print(f'The largest element is: {largest_ele}')

def rotate_arr_left(arr,position):
    length = len(arr)
    if position > length:
          position = position % length
          return position
    
    rotate_arr = arr[position:] + arr[:position]
    return rotate_arr

def reverse_array(arr):
     reversed_arr = arr[::-1]
     return reversed_arr

array_str = input("Enter the values: ")
array_list = array_str.split()
input_arr = [int(x) for x in array_list]
position = int(input("Enter the position:"))
rotate = rotate_arr_left(input_arr,position)
rrotate = reverse_array(input_arr)
print(f'{rotate}')
print(f'{rrotate}')

def split_and_rotate(arr,split_index):
  rotated_arr = arr[split_index:] + arr[:split_index]
  return rotated_arr

array = [1, 2, 3, 4, 5]
split_index = 2
rotated = split_and_rotate(array,split_index)
print("Rotated array: ", rotated)

def find_remainder(arr,n):
    product = 1
    for ele in arr:
        product = (product*ele) % n

    return product

array = [1,4,5,6,7,6,8,2,3]
n=7
remains = find_remainder(array,n)
print(f'Remainder: {remains}')'''