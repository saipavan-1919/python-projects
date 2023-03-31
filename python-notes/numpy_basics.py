"""
    Numpy module:
        * numpy module is known as numerical python
        * In python we have list as a datatype (this is dynamic data type)
        * In python there is no concept called arrays (as in c programming)
        * So numpy module provides us the arrays concept in python
        creating a array:
            numpy has a method called array it creates ndarray object
            syntax: <var> = numpy.array(<list>)
                    type of varaible will be = numpy.ndarray
        properties of ndarray object:
            1) size:
                var.size -> this will show total how many elements are in the array
            2) shape:
                var.shape -> this shows the shape of the array means rows and columns
                    if it is one dimensional array then it will show no.of elements
                    if it is two dimensional array then it will show no.of rows and columns as tuple
            3) ndim:
                var.ndim -> this shows the no.of dimensions in the array
            4) dtype:
                var.dtype -> this show what is overall data type of the elements in the array

        * Accessing elements in the ndarray is also simialr to the accessing of list elements

        Slicing of ndarray using indexing :
            * syntax:
                <nd_array_var>[row_lwr:row_upr, col_lwr:col_upr]
            * when we create ndarray using numpy it will be treated as a matrix
            * we can extract the sub-matrix using the slicing availble
            ex: 3*3 matrix  ===> matrix[0:3, 0:3]
                matrix = numpy.array([[1,2,3],[4,5,6],[7,8,9]]) # this is a 3*3 matrix
                if we want first 2 rows and 3 columns then 
                matrix[0:2,0:3]   => this gives 2*3 matrix
                 c1  c2   c3
                [ 1,  2,  3]   -> row 1
                [ 4,  5,  6]   -> row 2
                [ 7,  8,  9]   -> row 3

        Constructing 2D array using ndarray function:
            * we can create a ndarray object by passing a list two np.array function
            * But if we want to just create a empty 3*3 array then we can use ndarray function
             and created that required array
            * syntax:
                np.ndarray(shape=(rows,columns), dtype=<data_type>)
                * if we dont mention any data type then by default it is constructing a float data type array
                * when we construct a ndarray of int datatype then it is storing some random values in the array
                    I think this is working similar to array creation in C programming (garbage values)
            
"""

import numpy as np

my_list = [1,2,43,4,5]
# creating a ndarray element
arr = np.array(my_list)
print(arr)
print(type(arr))

# properties of ndarray object
# size of array 
print(arr.size)
# shape of array
print(arr.shape)
# dimensions in array
print(arr.ndim)
# data type of the elements in the array
print(arr.dtype)


# creating a two dimensional array (2D - array)
matrix = np.array([[1,2,3],[4,5,6]])
print("matrix = ",matrix)
print("dtype = ",matrix.dtype)
print("size = ",matrix.size)
print("shape = ",matrix.shape)
print("dimesions = ",matrix.ndim)


# printing elements in the ndarray using the loops
# for single dimensional array
for i in arr:
    print(i, end=" ")
print()
#for multi dimensional array
for i in matrix:
    print(i) # this is sub-array in the array
    for j in i:
        print(j, end=" ") # this will print each element by element
    print()



# slicing a matrix
matrix1 = np.array([[1,2,3],[4,5,6],[12,3,4]])
print(matrix1)
# slicing matrix into 2*3
print(matrix1[0:2,0:3])
# getting last two rows
print(matrix1[1:3,0:3])
# getting last two rows and two columns
print(matrix1[1:3,1:3])



# constructing a 2D array using the ndarray function
matrix2 = np.ndarray(shape=(2,3))
print(matrix2)
print(matrix2.dtype)
# constructing a 2D array of integer data type
matrix3 = np.ndarray(shape=(3,3),dtype=int)
print(matrix3)
print(matrix3.dtype)
print(matrix3.size)
print(matrix3.ndim)
print(matrix3.shape)
