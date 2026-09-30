import numpy as np
a=np.array([[1,2,3],[0,0,0],[1,1,1]])
print("DOT",np.dot(a,a))
print("Dimensions:",a.shape)
print("Slicing",a[1,2]) # this is as simple as normal indexing in python a[1][2]
print("Rows:",a[1]) # this is as simple as normal indexing in python a[1]
print("Columns:",a[:,2]) #this gives the matrice columns
b=np.array([[1,2,3],[0,0,0]])
print("Element-wise multiplication:",a*b[:,None]) # this is element wise multiplication :,None] this is streching column [None:,] row wise