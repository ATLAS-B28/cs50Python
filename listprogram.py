def interchange_first_last(arr):
     arr[0],arr[-1] = arr[-1],arr[0]
     return arr

array = [2,3,4,5,6]
print(f'Swapped: {interchange_first_last(array)}')