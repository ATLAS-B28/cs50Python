'''def interchange_first_last(arr):
     arr[0],arr[-1] = arr[-1],arr[0]
     return arr

array = [2,3,4,5,6]
print(f'Swapped: {interchange_first_last(array)}')

def swap_2_ele(list,pos1,pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list

list_1 = [2,3,4,5,6,7,8,1]
pos1 = 2
pos2 = 5
print(f'{swap_2_ele(list_1,pos1,pos2)}')

def find_ele(lst,ele):
    try:
        lst.index(ele)
        print(f'At position: {lst.index(ele)}')
        return True
    except:
        return False
        raise

lst = [2,3,5,7,8,9]
ele = int(input("Enter the number: "))
print(f'Original list: {lst}')
print(f'{find_ele(lst,ele)}')
    

list1 = [11, -21, 0, 45, 66, -93]
def negative_number_list(list):
 for i in list:
     if i < 0:
         print(f'{i}')

negative_number_list(list1)



import numpy as np
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
 
# result will be 3x4
 
result= [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

result = np.dot(A,B)
for r in result:
    print(f'{r}')

#If a is an N-D array and b is an M-D array (where M>=2), it is a sum product over the last axis of a and the second-to-last axis of b:
# dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])

The equation you provided represents the calculation of the dot product between arrays a and b. It involves summing the element-wise multiplication of specific axes of the two arrays.

Let's break down the equation and explain it in detail:

dot(a, b)[i, j, k, m]: This notation represents the element at index [i, j, k, m] in the resulting dot product array.

sum(a[i, j, :] * b[k, :, m]): This part of the equation calculates the sum of the element-wise multiplication between the selected axes of a and b.

a[i, j, :] selects the elements from the last axis of a corresponding to indices i and j. This can be thought of as selecting a specific row in the matrix a.

b[k, :, m] selects the elements from the second-to-last axis of b corresponding to indices k and m. This can be thought of as selecting a specific column in the matrix b.

a[i, j, :] * b[k, :, m] represents the element-wise multiplication between the selected row from a and the selected column from b.

sum(a[i, j, :] * b[k, :, m]) calculates the sum of the element-wise products, resulting in a single scalar value.

Therefore, the overall equation computes the dot product between a and b by summing the element-wise products over the last axis of a and the second-to-last axis of b. The resulting dot product array will have indices [i, j, k, m] and contain the summed values for each combination of those indices.

Note: The dot() function in numpy is generally used for matrix multiplication between two arrays of compatible dimensions. The equation you provided is a general representation of the dot product calculation rather than the exact usage of the dot() function.

'''