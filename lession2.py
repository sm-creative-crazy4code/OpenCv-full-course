# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np

# arrays are 0 indexed 
arr= np.array([(1,2,3),(4,5,6)])
# print value at a particular index
print(arr[1][1])
# : means printig all the valuest--> order rows then cols
print(arr[:])
# eg:print 0th col oof every row
print(arr[:,0])
# first row but all columns
print(arr[1,:])
# thing after coloumn is excluded
# getting a range of values
print(arr[0,1:3])
# 0th row form index 1 to 2

# reversing the array
print(arr[::-1])

# reshaping the array but dimension should be same
arr1=arr.reshape(3,2)
print(arr1)
arr1=arr.reshape(1,6)
print(arr1)

# appending an element
arr1=np.append(arr,9)
print(arr1)
# deleting an element=takes position
arr1=np.delete(arr,1)

# flattening or raveling operations.this will  give a 1d array but reshape gives 2d arrays
arr1=arr.ravel()

# concat
arr=np.array([2,3,4,6,5])
arr1=np.array([1,3,2])
print(np.concatenate((arr,arr1)))

# transpose
arr3=np.array([(2,3,4,6,5),(22,13,24,46,5)])
print(np.transpose(arr3))

# copying array
arr1=np.copy(arr)








