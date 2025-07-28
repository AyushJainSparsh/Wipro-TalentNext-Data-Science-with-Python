# Exercise 1: Create two dimensional 3*3 array and perform ndim, shape, slicing operation on it.

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Array:", arr)
print("Number of dimensions:", arr.ndim)
print("Shape of the array:", arr.shape)
print("Sliced array (first two rows):\n", arr[:2,:2])

# Exercise 2: Create one dimensional array and perform ndim,shape, reshape  operation on it.

import numpy as np
arr1d = np.array([10, 20, 30, 40, 50, 60])
print("1D Array:", arr1d)
print("Number of dimensions:", arr1d.ndim)
print("Shape of the array:", arr1d.shape)
reshaped_arr = arr1d.reshape(2, 3)
print("Reshaped array (2x3):\n", reshaped_arr)

