#!/usr/bin/env python
# coding: utf-8

# # Extended Graham scan algorithm

# Use the cell below for all python code needed to realise the extended Graham scan algorithm (including any auxiliary data structures and functions you might need). The `extendedgrahamscan()` function itself should take as input parameter a list of 2D points (`inputSet`), and return the subset of such points that lie on the convex hull (`outputSet`).

# In[1]:


def extendedgrahamscan(inputSet):
    outputSet = []
    return outputSet


# Use the cell below for all python code needed to generate test data points (both random and those representing worst-case scenario).

# In[2]:


import random

#code for random data generation
def randGeneration(n):
    return [[random.randint(0, 32767), random.randint(0, 32767)] for i in range(n)]

#code for worst case data generation
def randWorstGeneration(n):
    return [[0,0] for i in range(n)]


# Use the cell below for all python code needed to test the `extendedgrahamscan()` function on the data generated above.

# In[1]:


import timeit

#test code
def test(n, worstCase = False):
    timetaken = [0 for i in range(len(n))]
    for i in n:
        data = randWorstGeneration(int(i)) if worstCase else randGeneration(int(i))
        start_time = timeit.default_timer()
        _ = extendedgrahamscan(data)
        timetaken[n.index(i)] = timeit.default_timer() - start_time
    return timetaken

n = [1e2, 5e2, 1e3, 5e3, 1e4, 1.5e4, 2e4]
r_timetaken, w_timetaken = test(n), test(n, worstCase = True)


# *Optional*: Feel free to use the code below on small datasets (e.g., N = 10) to visually inspect whether the algorithm has been implemented correctly. The fragment below assumes both `inputSet` and `outputSet` to be lists of 2D points, with each point being a list of 2 elements (e.g., `[[x1,y1], [x2,y2], ..., [x_k,y_k]]`)

# In[2]:


import matplotlib.pyplot as plt

#inputSet = [[1,1], [2,2], [3,3], [4,4], [1,4], [3,1], [1,5], [2,4], [3,5]]
#outputSet = [[1,1], [3,1], [4,4], [3,5], [1,5]]

#k = 100
#inputSet = randGeneration(k)
#outputSet = extendedgrahamscan(inputSet)

plt.figure()

#first do a scatter plot of the inputSet
input_xs, input_ys = zip(*inputSet)
plt.scatter(input_xs, input_ys)

#then do a polygon plot of the computed covex hull
outputSet.append(outputSet[0]) #first create a 'closed loop' by adding the first point at the end of the list
output_xs, output_ys = zip(*outputSet) 
plt.plot(output_xs, output_ys) 

plt.show() 


# In[ ]:




