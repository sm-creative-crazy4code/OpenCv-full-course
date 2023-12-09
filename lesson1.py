# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np


# checking version to esure that no problem is there 
print(np.__version__)

# # 1 d row vector
arr= np.array([1,2,3])
print(arr)
# col-vector
avv_v=np.array([[1],[3],[4]])
print(avv_v)

# # 2-d by passing tuples
arr3= np.array([[(1,2,3),(3,4,5)],[(0,2,4),(9,4,5)]])
print(arr3)

# # fill the array with 0s
arr=np.zeros((3,3),dtype="uint8")
print(arr)

# # crearte an array filled with 1s
arr=np.ones((3,3),dtype="uint8")
print(arr)

# # fill with any random value
aarr=np.full((3,3),5)
print(aarr)

# # generate idnetity matirix
arr= np.eye(3)
print(arr)

# range arrays
arr=np.arange(0,10,6)
print(arr)
# gives value in range 0 to 10 (execluded )at a distance of6 each

# devide a given range into some equal spaces
arr= np.linspace(0,2,9)
print(arr)
# # here two and 9 are included

# # random fuction for adding noise to image
arr= np.random.rand(2,3)
# # generates a random matrix of 2*3 with values b/w 0-1
# # scaler multiplication with k can be done as np.random.rand(2,3)*k
# print(arr)

# # random intergere matrix genrater max vlaue is 5
arr= np.random.randint(5,size=(3,3))
print(arr)

# array inspection
arr3= np.array([[(1,2,3),(3,4,5)],[(0,2,4),(9,4,5)]])
print(arr3.shape)
print(arr3.size)
print(arr3.dtype)

# typecasting in arr
# arr1=arr3.astype(float)

# intensity increasing==>matrix addtion
# matrix addition
arr_f=arr1+arr3
# same for -,*,/








