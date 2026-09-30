import numpy as np
a=np.array([[1,2,3],[1,2,3],[1,2,3]]) 
b=np.array([[1,2,3],[1,2,3],[1,2,3]])
# c=np.dot(a,b) #this is equal to a*b and matmul(a,b).
c=np.matmul(a,b) #this is equal to a*b and dot(a,b).
print(c)

# 2D arrays - identical results
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("dot is:", np.dot(a, b))      # Matrix multiplication
print("matmul is:", np.matmul(a, b))   # Same result
print(a @ b)             # Alternative syntax for matmul


# 3D arrays - different behavior
a3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
b3d = np.array([[[1, 0], [0, 1]], [[2, 0], [0, 2]]])

np.dot(a3d, b3d)      # Shape: (2, 2, 2, 2) - sum over last/first axis
np.matmul(a3d, b3d)   # Shape: (2, 2, 2) - matrix ops on last 2 dims

# Scalars
np.dot(5, a)          # Works - scalar multiplication
# np.matmul(5, a)       # Error!
