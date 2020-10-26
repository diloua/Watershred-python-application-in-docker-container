import numpy as np
import csv
from numpy import genfromtxt
from collections import deque
import sys 
import os
#Function to get pixels neighbors    
def neighbors(height, width, pixel, size):
    return np.mgrid[
         max(0, pixel[0] - 1):min(height, pixel[0] + size),
         max(0, pixel[1] - 1):min(width, pixel[1] + size)
      ].reshape(2, -1).T


fifo = deque()
mask = -2
wshed = 0
init = -1
inqueue = -3
level_indices = []

# Initialization :

current_label = 0
level_value = 0

#Getting the data from the txt file 
input_file = "input/" + sys.argv[1] 
my_data = genfromtxt(input_file, delimiter=',', dtype='int') #Ref


total_size = my_data.size 
r_size = np.size(my_data, 1)
c_size = np.size(my_data, 0)

#Using the reshape function to transform the 2D so that it can be processed
reshaped_data = my_data.reshape(total_size)

#Creating a 2D array and filling it of -1
labels = np.zeros((r_size, c_size), dtype='int')
labels.fill(-1) 

#Sorting data in increasing order
indices = np.argsort(reshaped_data)
sorted_data = reshaped_data[indices]

#Initiliazing the pairs of pixels using mgrid
pixels = np.mgrid[0:r_size, 0:c_size].reshape(2, -1).T

#Sorting the pair of pixels in incresing order
sorted_pixels = pixels[indices]

#Getting the neighbours for each pixel 
neighbours_list = np.array([neighbors(r_size, c_size, p, int(sys.argv[2])) for p in pixels])
reshaped_n = neighbours_list.reshape(r_size, c_size)

#Getting the level indices 
for i in range(total_size):
    for p in pixels:
        if sorted_data[i] > sorted_data[level_value]:
            level_value = i
            level_indices.append(i)
level_indices.append(total_size)


#Execution of the algorithm 

i = 0 # We start with the index 0
for j in level_indices:
    for p in sorted_pixels[i:j]:
        labels[p[0], p[1]] = mask
        for q in reshaped_n[p[0], p[1]]:
            if labels[q[0], q[1]] > 0  or labels[q[0], q[1]] == wshed:
                labels[p[0], p[1]] = inqueue
                fifo.append(p)
                break
    while(fifo):
        #p = queue.get()
        p = fifo.popleft()
        for q in reshaped_n[p[0],p[1]]:
            if labels[q[0],q[1]] > 0:
                if labels[p[0] , p[1]] == inqueue or (labels[p[0],p[1]]==wshed and flag == True):
                    labels[p[0], p[1]] = labels[q[0], q[1]]
                elif labels[p[0], p[1]] > 0 and labels[p[0],p[1]] != labels[q[0],q[1]]:
                    labels[p[0],p[1]] = wshed
                    flag = False 
            
            elif labels[q[0],q[1]] == wshed:
                if labels[p[0],p[1]] == inqueue:
                    labels[p[0],p[1]] = wshed
                    flag = True
            elif labels[q[0], q[1]] == mask:
                    labels[q[0], q[1]] = inqueue
                    fifo.append(q)

    for p in sorted_pixels[i:j]:
        if labels[p[0], p[1]] == mask:
            current_label = current_label+1
            fifo.append(p)
            labels[p[0], p[1]] = current_label
            while (fifo):
                q = fifo.popleft()
                for r in reshaped_n[q[0],q[1]]:
                     if labels[r[0], r[1]] == mask:
                         fifo.append(r)
                         labels[r[0], r[1]] = current_label
    i = j

file_split = os.path.splitext(sys.argv[1])[0]
print(labels)
file_name = "output/" + file_split + "_wt_" + sys.argv[2] + ".txt"
np.savetxt(file_name, labels, delimiter=',', fmt='%d')
