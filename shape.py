import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
#a = np.array([[1], [2], [3]])
#b = np.array([[4], [5], [6]])

print(np.r_[a, b]) # [1 2 3 4 5 6]
print(np.hstack([a, b])) # [1 2 3 4 5 6]

print(np.r_[[a], [b]]) # [[1 2 3], [4 5 6]]
print(np.vstack([a, b])) # [[1 2 3], [4 5 6]]
print(np.row_stack([a, b])) # [[1 2 3], [4 5 6]]

print(np.c_[a, b]) # [[1 4], [2 5], [3 6]]
print(np.column_stack([a, b])) # [[1 4], [2 5], [3 6]]

print(np.dstack([a, b])) # [ [[1 4], [2 5], [3 6]] ]

aa, bb = np.meshgrid(a, b)
print(aa) # [[1 2 3], [1 2 3], [1 2 3]]
print(bb) # [[4 4 4], [5 5 5], [6 6 6]]
print(np.c_[aa.ravel(), bb.ravel()]) # [[1 4], [2 4], [3 4], [1 5], [2 5], [3 5], [1 6], [2 6], [3 6]]

'''
stack : Join a sequence of arrays along a new axis.
vstack : Stack arrays in sequence vertically (row wise).
hstack : Stack arrays in sequence horizontally (column wise).
dstack : Stack arrays in sequence depth wise (along third dimension).
concatenate : Join a sequence of arrays along an existing axis.
vsplit : Split array into a list of multiple sub-arrays vertically.
hsplit : Split array along second axis.
block : Assemble arrays from blocks.
'''
