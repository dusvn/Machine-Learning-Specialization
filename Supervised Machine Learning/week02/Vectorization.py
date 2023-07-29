import numpy as np 
import time 
"""
a = np.zeros(4)
print(f"Type of data {a.dtype}")
print(f"Data in a {a}")
print(f"Num of elements {a.shape}")
print("=======")
a = np.zeros((4,))
print(f"Type of data {a.dtype}")
print(f"Data in a {a}")
print(f"Num of elements {a.shape}")
print("=======")
a = np.random.sample(4) 
print(f"Type of data {a.dtype}")
print(f"Data in a {a}")
print(f"Num of elements {a.shape}")
print("=======")

a = np.arange(1,10,2)
print(f"Type of data {a.dtype}")
print(f"Data in a {a}")
print(f"Num of elements {a.shape}")
print("=======")

a = np.random.rand(4)
print(f"Type of data {a.dtype}")
print(f"Data in a {a}")
print(f"Num of elements {a.shape}")
print("=======")
#If we have printed shape like (4,) that means we have 1d array 

print("User specific values:")
specific = np.array([1,2,3,4])
specific1 = np.array([1.,2.,3.,5,10])
print(f"Specific example : {specific},{specific1}")

# =============
temp = np.arange(10)
print(f"{temp},shape {temp.shape},temp[1] = {temp[1]},last element in array = {temp[-1]}")

try: 
    c = temp[10]
except Exception as e: 
    print("Error message:")
    print(e) 

"""
"""
a = np.arange(10)
print(f"a = {a}")

print(f"a[0:end:1] ={a[:len(a):1]}")
print(f"a[0:end:1] ={a[3:]}")
print("Take all element bellow index 3 ")
print(f"a[0:end:1] ={a[:3]}")
print("Take all elements above index 3")
print(f"{a[3:]}")

sum = np.sum(a)
mean = np.mean(a)
negative = -a
positive = negative**2 
print(f"Sum:{sum},mean:{mean},negative:{negative},positive {positive}")
"""
"""
print("Wise operator:")
a = np.array([1,2,4,5])
b = np.array([1,-1,1,2])
print(f"a ={a},b = {b} , a+b = {a+b}")
a = 5*a 
print(f"{a}")
"""

#Dot
# The result of this is scalar becous we do vectorize dot is not like * becouse operator * will do x[0]*y[0] for this all values 
"""
a = np.array([1,2,3,4])
b = np.array([1,2,3,5])
c = np.dot(a,b) 
print(f"Dot result is:{c},shape of new element is {c.shape}")


# show common Course 1 example
X = np.array([[1],[2],[3],[4]])
w = np.array([2])
c = np.dot(X[1], w)

print(f"X[1] has shape {X[1].shape}")
print(f"w has shape {w.shape},w ={w}")
print(f"c has shape {c.shape}, c={c}")

l = np.zeros((2,5))
l[0][1] = 1
print(l)
"""
a = np.arange(6)
print(a)
a=a.reshape(6,1)
# this function will take og array and reshape it --> new array will have 6 rows with one element 
print(a)