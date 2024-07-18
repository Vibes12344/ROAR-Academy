import numpy as np
#1 
# Given vector
v = np.array([2., 2., 4.])

# Coordinate axes
e0 = np.array([1., 0., 0.])
e1 = np.array([0., 1., 0.])
e2 = np.array([0., 0., 1.])

# Projections onto the axes
projection_e0 = np.dot(v, e0)
projection_e1 = np.dot(v, e1)
projection_e2 = np.dot(v, e2)

print(projection_e0, projection_e1, projection_e2)
#2 
a = np.array([[6,-9,1],
             [4,24,8]])
b = 2
product = a*b
print(product)

#3 
a1 = np.array([[0,1,2,3,4,5],
               [10,11,12,13,14,15],
               [20,21,22,23,24,25],
               [30,31,32,33,34,35]
               [40,41,42,43,44,45],
               [50,51,52,53,54,55]])
