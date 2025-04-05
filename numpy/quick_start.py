# START:: An Example
# import matplotlib
# import numpy as np
# a = np.arange(15).reshape(3,5)
# print(
#     a.ndim, 
#     a.shape, 
#     a.size, 
#     a.dtype.name, 
#     a.itemsize, 
#     a.data
#     )
# b = np.array([1,2,3])
# print( type(b) )
# ----------------

# START :: Array Creation
# import numpy as np
# from numpy import pi
# a = np.array([2,3,4])
# b = np.array([2.4, 4.1, 7.2])
# print(
#     a.dtype,
#     b.dtype.name,
#     a.itemsize,
#     b.itemsize,
#     )
# c = np.array([(1.5,2,3), (4,5,6)])
# print(c, c.dtype.name)
# d = np.array([
#     [1,2],
#     [3,4]
# ], dtype=int)
# print(d)
# with_zeros = np.zeros((3,5))
# with_ones = np.ones((5,3), dtype=np.int16)
# with_empty = np.empty((6,4), dtype=int)
# print(with_zeros, with_ones, with_empty)

# arange1 = np.arange(10, 30, 5)
# arange2 = np.arange(0, 2, .3)
# print(arange1, arange2)

# linspace1 = np.linspace(0,4,4)
# linspace2 = np.linspace(0,2*pi, 100)
# sinx = np.sin(linspace2)
# print(linspace1, sinx)
# ---------------------

# START :: Printing Arrays
# import numpy as np
# import sys
# np.set_printoptions(threshold=sys.maxsize)
# one_d = np.arange(6) # 1d
# print(one_d)

# two_d = np.arange(12).reshape(4,3)
# print(two_d)

# three_d = np.arange(24).reshape(2,3,4)
# print(three_d)

# big_d = np.arange(10000).reshape(100, 100)
# print(big_d)
# ---------------------

# START :: Basic Operations
# import numpy as np
# from numpy import pi
# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# c = a - b
# d = b**2
# e = 10 * np.sin(a)
# elementwise_product = a * b
# product1 = a @ b
# product2 = a.dot(b)
# # print(c, d, e, elementwise_product, product1, product2)
# rg = np.random.default_rng(1) #create instance of default random number generator
# ones = np.ones((2,3), dtype=int)
# random = rg.random((2,3))
# # ones_product_three = a * 3
# another_ones = np.ones(3, dtype=int)
# another_linspace = np.linspace(0, pi, 3)
# print(another_linspace.dtype.name)
# addition = another_ones + another_linspace
# f = np.exp(c * 1)
# x = np.linspace(4, 8, 2);
# arr = np.arange(12).reshape(3,4)
# print(ones, random, a, addition, f, arr.sum(axis=1), x.min(), x.max())
# --------------------

# START :: Universal Functions
# import numpy as np
# b = np.arange(3)
# exp = np.exp(3)
# sqrt = np.sqrt(b)
# c = np.array([2, -1, 4])
# np.add(b, c)
# print(b)
#  -----------------

# START:: Indexing, Slicing & Iterating
# import numpy as np
# def f(x,y):
#     return 10 * x + y
# a = np.arange(10)**3
# print(a[2])
# print(a[::-1])
# b = np.fromfunction(f, (5,4), dtype=int)
# c = np.array([
#         [
#             [0,1,2],
#             [10, 12, 13],
#         ],
#         [
#             [100, 101, 102],
#             [110, 112, 113]
#         ]
#     ]
# )
# print(c.shape)
# print(b,  b[1:3, :], b[-1, ...])
# for element in b.flat:
#     print(element, end="\n")
#  ----------------------

# Shape Manipulation
# START :: Changing the shape of an array
# import numpy as np
# rg = np.random.default_rng(1)
# a = np.floor(10 * rg.random((3,4)))
# print(a.resize((2, 6)))
# -------------

# START :: Stacking Together in differant ways
# import numpy as np
# from numpy import newaxis
# rg = np.random.default_rng(1)
# a = np.floor(10 * rg.random((2,2)))
# b = np.floor(10 * rg.random((2,3)))

# print( np.column_stack((a,b)) )
# print( np.hstack((a, b)) )

# r = np.r_[1:4, 0, 4]
# c = np.c_[1:10, 0, 1]
# print(r)
# np.vstack((a, b))
# np.column_stack((a, b))

# START :: Splitting one array into several smaller ones
# import numpy as np
# rg = np.random.default_rng(1)
# a = np.floor(10 * rg.random((2, 12)))
# print( np.hsplit(a, (3, 4)) )
# -----------------

# START :: COpies and views
# import numpy as np
# a = np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ])
# b = a
# print( b is a )
# -------------------

# START :: View or shallow copy
# import numpy as np
# a = np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ])
# b = a.view()
# print(a is b)
# print(b.base is a)
# b.reshape((2,6))
# print(b)
# --------------------

# START :: Deep Copy
# import numpy as np
# a = np.array([
#     [1,2,3,4],
#     [5,6,7,8]
# ])


# START :: ------
# import numpy as np
# a = np.arange(10) ** 3
# print(a[::-1])
# def f(x, y):
#     return 10 * x + y
# b = np.fromfunction(f, (10, 8), dtype=int)
# print(b)
# print(b[2, 3])
# print(b[0:5, 1])
# print(b[:, 1])
# print(b[1:3, :])
# print(b[-1])

# for row in b:
#     print(row)
# list = []
# for element in b.flat:
#     list.append(element)
# print(list)
#  END ---------------

# START :: Deep Copy
# import numpy as np
# a = np.arange(int(1e8))
# print( 1e3 )
#  END -----

# START :: Functions and methods overview
import numpy as np
a = np.arange(30)
b = a.reshape((2, -1, 3))
print(b)