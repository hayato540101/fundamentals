np.r_ np.vstack関数と同じように使える。 # vertical

import numpy as np

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

np.r_[a1,a2]
# array([1, 2, 3, 4, 5, 6])

np.r_[90, 8.0, 70, np.array([2,55,]), 100]
# array([ 2. ,  5. ,  3. ,  2. ,  3. ,  4.2])


b1 = np.ones((6,3)) # axis=1方向の要素数がdと一致

b2 = np.zeros((1, 3)) # axis=0方向の要素数はcと同じ2である必要はない。  

np.r_[b1, b2]
np.r_[b1, b2].shape

c = np.ones((3, 4))

np.r_[b2, c]
ValueError: all the ray dimensions except for the concatenation axis must match exactl

np.c_ np.hstackに対応する # horizontal

a3 = np.array([1,3])
a4 = np.array([1,10])

np.c_[a3,a4]
np.c_[a3,a4].shape # (2, 2)
array([[ 1,  1],
       [ 3, 10]]) # 横方向に結合している


b3 = np.zeros([4,7])
b4 = np.ones([4,2])

np.c_[b3,b4]
np.c_[b3,b4].shape # (2, 2)

array([[0., 0., 0., 0., 0., 0., 0., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1.]])
>>> np.c_[b3,b4].shape # (2, 2)
(4, 9)
