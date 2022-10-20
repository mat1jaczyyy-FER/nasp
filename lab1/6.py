import numpy as np

vector_a = np.array([1, 3, 5])
vector_b = np.array([2, 4, 6])

mat_mul = vector_a @ vector_b.T
vect_dot = np.dot(vector_a.T, vector_b)
mat_exp = mat_mul ** 2
sub_mat = mat_exp[1:, 1:]
