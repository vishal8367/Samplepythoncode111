import numpy as np
arr=np.array([1,2,3,4,5],dtype='S')
print(arr)
print(arr.dtype)

#
arr=np.array([1.1,2.1,3.1])
new=arr.astype(int)
print("New array is :",new)
print("New array datatype :",new.dtype)

