import numpy as np
from numpy.linalg import eig

a = np.array([[-6,3],
             [4,5]])

w,v = eig(a)
print(f'E-value:{w} E-Vector:{v}')

a = np.array( [[2, 2, 4],
             [1, 3, 5], 
             [2, 3, 4]])

#identity matrix for n = 3
i3 = np.identity(3) 

i3 * a


w,v = eig(a)
print(f'E-value:{w} E-Vector:{v}')