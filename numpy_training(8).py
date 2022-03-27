# -*- coding: utf-8 -*-
"""Untitled59.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nO9emPUb2dix7yl4Z7shshkniFCL9jTa
"""

# Let’s see another example of reshaping a NumPy array from lower to higher
# dimensions. The following script defines a NumPy array of shape (4,6). The original ar
# is then reshaped to a three-dimensional array of shape (3, 4, 2). Notice here
# again that the product of dimensions of the original array (4 x 6) and the
# reshaped array (3 x 4 x 2) is the same, i.e., 24.
import numpy as np
print("two-dimensional array")
two_d_array = np.random.randint(1,20, size = (4,6))
print(two_d_array)
print("\nthree-dimensional array")
three_d_array = np.reshape(two_d_array,(3,4,2))
print(three_d_array)

# Let’s try to reshape a NumPy array in a way that the product of dimensions
# does not match. In the script below, the shape of the original array is (4,6).
# Next, you try to reshape this array to the shape (1,4,2). In this case, since
# the product of dimensions of the original and the reshaped array don’t match,
# you will see an error in the output.
import numpy as np
print("two-dimensional array")
two_d_array = np.random.randint(1,20, size = (4,6))
print(two_d_array)
print("\nthree-dimensional array")
three_d_array = np.reshape(two_d_array,(1,4,2))
print(three_d_array)

# Let’s now see a few examples of reshaping NumPy arrays from higher to
# lower dimensions. In the script below, the original array is of shape (4,6)
# while the new array is of shape (24). The reshaping, in this case, will be successful
# since the product of dimensions for original and reshaped arrays is the same.
import numpy as np
print("two-dimensional array")
two_d_array = np.random.randint(1,20, size = (4,6))
print(two_d_array)
print("\none-dimensional array")
one_d_array = two_d_array.reshape(24)
print(one_d_array)

# Finally, to convert an array of any dimensions to a flat, one-dimensional
# array, you will need to pass —1 as the argument for the reshaped function, as
# shown in the script below, which converts a two-dimensional array to a one dimensional
# array.
import numpy as np
print("two-dimensional array")
two_d_array = np.random.randint(1,20, size = (4,6))
print(two_d_array)
print("\none-dimensional array")
one_d_array = two_d_array.reshape(-1)
print(one_d_array)

# Similarly, the following script converts a three-dimensional array to a one dimensiona
# array.
import numpy as np
print("two-dimensional array")
three_d_array = np.random.randint(1,20, size = (4,2,6))
print(three_d_array)
print("\non-dimensional array")
one_d_array = three_d_array .reshape(-1)
print(one_d_array)

# NumPy arrays can be indexed and sliced. Slicing an array means dividing an
# array into multiple parts. NumPy arrays are indexed just like normal lists.
# Indexes in NumPy arrays start from 0, which means that the first item of a
# NumPy array is stored at the 0th index. The following script creates a simple
# NumPy array of the first 10 positive integers.
import numpy as np
s = np.arange(1,11)
print(s)

# The item at index one can be accessed as follows:
import numpy as np
s = np.arange(1,11)
print(s)
print(s[1])

# To slice an array, you have to pass the lower index, followed by a colon and
# the upper index. The items from the lower index (inclusive) to the upper
# index (exclusive) will be filtered. The following script slices the array “s”
# from the 1st index to the 9th index. The elements from index 1 to 8 are
# printed in the output.
import numpy as np
s = np.arange(1,11)
print(s)
print(s[1:9])

# If you specify only the upper bound, all the items from the first index to the
# upper bound are returned. Similarly, if you specify only the lower bound, all
# the items from the lower bound to the last item of the array are returned.
import numpy as np
s = np.arange(1,11)
print(s)
print(s[:5])
print(s[5:])

# Array slicing can also be applied on a two-dimensional array. To do so, you
# have to apply slicing on arrays and columns separately. A comma separates
# the rows and columns slicing. In the following script, the rows from the
# first and second indexes are returned, while all the columns are returned.
# You can see the first two complete rows in the output.
import numpy as np
row1 = [10,12,13]
row2 = [45,32,16]
row3 = [45,32,16]
nums_2d = np.array([row1, row2, row3])
print(nums_2d[:2,:])
