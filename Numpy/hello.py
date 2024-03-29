import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(a[0])

#? array filled with zeroes
# print(np.zeros(2))

#? array filled with ones
# print(np.ones(3))

#? empty array
# print(np.empty(4))

#? array with a range of elements
# print(np.arange(6))

#! (first number,last number,step size)
# b = np.arange(2,9,2)
# print(b)

#* specifying data type default data type is float64
# x = np.ones(2, dtype=np.int64)

#? 2d array
# z = np.zeros((3,4))
# print(z)

#? reshaping an array
# np.set_printoptions(threshold=sys.maxsize) [this statement is use to print full size of the array] 
# print(np.arange(10000).reshape(100,100))

#! Basic Operators
# a = np.array([20,30,40,50])
# b = np.arange(4)
# c = a - b
# print(c)

# squaring every elements
# d = b**2 
# print(d)
# sin of every elements
# print(np.sin(a))
# checks all the elements
# print(a<35)

# A = np.array( [[1,1],
#                [0,1]] )

# B = np.array([[2,0],
#               [3,4]] )

# elementwise product
# print(A*B)
# matrix product
# print(A@B)
# another matrix product method
# print(A.dot(B))

# sorting
arr = np.array([2,1,5,3,7,4,6,8])
print(np.sort(arr))

# concatenate
a = np.array([1,3,4,2])
b = np.array([5,7,8,6])
print(np.concatenate((a,b)))

# 2d concatenate
x = np.array([[1,2],[3,4]])
y = np.array([[5,6]])
print(np.concatenate((x,y), axis = 0))


arr_eg = np.array([[[0,1,2,3],
                    [4,5,6,7]],
                    
                    [[0,1,2,3],
                     [4,5,6,7]],
                     
                    [[0,1,2,3],
                     [4,5,6,7]]])
# number of dimensions
print(arr_eg.ndim)
# size
print(arr_eg.size)

# another way of reshaping
arr1 = np.arange(6)
# order: C means to read/write the elements using C-like index order, F means to read/write the elements using Fortran-like index order, A means to read/write the elements in Fortran-like index order if a is Fortran contiguous in memory, C-like order otherwise. (This is an optional parameter and doesn’t need to be specified.)
print(np.reshape(arr1, newshape=(1,6), order ='C'))

# how to add a new axis
arr2 = np.array([1,2,3,4,5,6])
print(arr2.shape)
arr3 = arr2[np.newaxis, :]
print(arr3.shape)

# converting in row vector and column vector
row_vec = arr2[np.newaxis, :]
print(row_vec.shape)
col_vec = arr2[:,np.newaxis]
print(col_vec.shape)

# changing index position to 1 
b0 = np.expand_dims(arr2, axis=1)
print(b0.shape)
c0 = np.expand_dims(arr2, axis=0)
print(c0.shape)

# indexing and slicing 
data = np.array([1,2,3])
print(data[1])
print(data[0:2])
print(data[1:])
print(data[-2:])
print(data[-3:])

d = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# unsorted result
print(a[a<5])
# sorted result
print(np.sort(d[d<5]))

five_up = (d >= 5)
print(d[five_up])

div_by_2 = d[d%2==0]
print(div_by_2)

c = d[(d > 2) & (a < 11)]
print(c)

fiveup = (d>5)|(d==5)
print(fiveup)

arrr=np.nonzero(d<5)
print(arrr)

list_of_coordinates = list(zip(arrr[0],arrr[1]))
for coord in list_of_coordinates :
    print(coord)

print(d[arrr])

# empty nonzero 
not_there = np.nonzero(d == 42)
print(not_there)

a1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr0 = a1[3:8]
print(arr0)

a2 = np.array([[1,1],
               [2,2]])

a3 = np.array([[3,3],
               [4,4]])

print(np.vstack((a2,a3)))
print(np.hstack((a2,a3)))

x = np.arange(1,25).reshape(2,12)
print(x)
print(np.hsplit(x,3))
print(np.hsplit(x,(3,4)))

# copying syntax: b = a.copy()

datas = np.array([1,2])
ones = np.ones(2, dtype=int)
print(datas + ones)
print(datas - ones)
print(datas * ones)
print(datas / ones)

r = np.array([1,2,3,4])
print(r.sum())

p = np.array([[1,1],[2,2]])
# row-wise sum
print(p.sum(axis=0))
# column-wise sum
print(p.sum(axis=1))

# broadcasting(vector and scalar opertions)
d1 = np.array([1.0,2.0])
print(d1*1.6)

a4 = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
               [0.54627315, 0.05093587, 0.40067661, 0.55645993],
               [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

print(a4.sum())
print(a4.min())
print(a4.max())
print(a4.min(axis=0)) # axis = 0 denotes column
print(a4.min(axis=1)) # axis = 1 denotes row

# creating matrix
data0 = np.array([[1,2],[3,4]])
print(data0)

# slicing
print(data0[0,1])
print(data0[1:3])
print(data0[0:2,0])
print(data0.max())
print(data0.min())
print(data0.sum())
# accessing rows and columns
print(data0.max(axis=0))
print(data0.max(axis=1))

# multi-dimensional array with ones
print(np.ones((4,3,2)))

# array with random values
rng = np.random.default_rng(0)
print(rng.random(3))

# random array with values between 0 to 4
print(rng.integers(5,size=(2,4)))

arr4 = np.array([11,11,12,13,14,15,16,17,12,13,11,14,18,19,20])
unique_values = np.unique(arr4)
print(unique_values)

unique_values, indices_list = np.unique(arr4, return_index=True)
print(indices_list)
unique_values, occurrence_count = np.unique(arr4, return_counts=True)
print(occurrence_count)

a_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[1,2,3,4]])
uniq_val = np.unique(a_2d)
print(uniq_val)

unique_rows = np.unique(a_2d, axis=0)
print(unique_rows)

unique_rows, indices, occurrence = np.unique(a_2d, axis=0, return_counts=True, return_index=True)
print(indices)
print(occurrence)

arr5 = np.arange(6).reshape((2,3))
print(arr5)
print(arr5.transpose())
print(arr5.T)

# reversing 1-D array
arr6 = np.array([1,2,3,4,5,6,7,8])
reversed_arr = np.flip(arr6)
print(reversed_arr)

# reversing 2-D array
arr7 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
reversed_arr_2d = np.flip(arr7)
print(reversed_arr_2d)

# reversing only rows
reversed_arr_rows = np.flip(arr7, axis=0)
print(reversed_arr_rows)
# reversing only columns
reversed_arr_cols = np.flip(arr7, axis=1)
print(reversed_arr_cols)

# reversing single row
arr7[1] = np.flip(arr7[1])
print(arr7)

# reversing single column
arr7[:,1] = np.flip(arr7[:,1])
print(arr7)

# flatting the multi-d array
x1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a5 = x1.flatten()
a5[0] = 99
print(x1)
print(a5)

a6 = x1.ravel()
a6[0] = 98
print(x1)
print(a6)

# mathematical formulas
predictions = np.array([1,1,1])
labels = np.array([1,2,3])
n = 3
error = (1/n) * np.sum(np.square(predictions - labels))

print(error)

a8 = np.array([1,2,3,4,5,6])
np.save('new',a8)
b1 = np.load('new.npy')
print(b1)

csv_arr = np.array([1,2,3,4,5,6,7,8])
np.savetxt('new_file.csv', csv_arr)
csv = np.loadtxt('new_file.csv')
print(csv)

a7 = np.array([[-2.58289208,  0.43014843, -1.24082018, 1.59572603],
               [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
               [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
               [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]])

df = pd.DataFrame(a7)
print(df)

df.to_csv('pd.csv')
data1 = pd.read_csv('pd.csv')
print(data1)

np.savetxt('np.csv',a7,fmt='%.2f',delimiter=',',header='1, 2, 3, 4')

a9 = np.array([2,1,5,7,4,6,8,14,10,9,18,20,22])
plt.plot(a9)
plt.show()

# x2 = np.linspace(0,5,20)
# y2 = np.linspace(0,10,20)
# plt.plot(x,y,'purple')
# plt.show()

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
plt.show()