#1-task

import numpy as np

original=[12.23,13.32,100,36.32]
arr=np.array(original)
print('Original List:',original)
print('One-dimensional NumPy array:',arr)

#2-task

import numpy as np

arr=np.array([2,3,4,5,6,7,8,9,10])
arr2=arr.reshape(3,3)
print(arr2)

#3-task

import numpy as np

zeros=np.zeros(10)
zeros[5]=11
print(zeros)

#4-task

import numpy as np

arr=np.arange(12,38)
print(arr)

#5-task

import numpy as np

arr=np.array([1,2,3,4])
floatarr=arr.astype(float)

print(floatarr)

#6-task

#6
import numpy as np

centigrade=np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0. ])
fahrenheit=centigrade*9/5 + 32
centigrade2=np.array([0, 12, 45.21, 34, 99.91,32])
cen_from_far=(centigrade2-32)*5/9
print('Values in Fahrenheit degrees:',fahrenheit)
print('Values in Centigrade degrees:',centigrade)
print('Values in Centigrade degrees:',cen_from_far)
print('Values in Fahrenheit degrees:',centigrade2)

#7-task

import numpy as np

original=np.array([10,20,30])
appendings=np.array([40,50,60,70,80,90])
arr=np.concatenate((original,appendings))
print(f'original array:{original}')
print(f'After append values to the end of the array:{arr}')

#8-task

import numpy as np
arr=np.random.rand(10)
mean=np.mean(arr)
median=np.median(arr)
standard_dev=np.std(arr)
print(f'Random array of 10 elements:{arr}')
print(f'Mean of 10 elements:{mean}')
print(f'Median of 10 elements:{median}')
print(f'Standard deviation of 10 elements:{standard_dev}')

#9-task

import numpy as np

arr=np.random.rand(10,10)
min=np.min(arr)
max=np.max(arr)
print(f'min value of 10x10 array:{min}')
print(f'max value of 10x10 array:{max}')

#10-task

import numpy as np

arr=np.random.rand(3,3,3)
print(arr)





