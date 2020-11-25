import numpy as np
import matplotlib.pyplot as plt


X = np.array(
    [[ 1. ,  2. ],
     [ 2. ,  2. ],
     [ 0. , -0.2],
     [ 2. ,  3. ],
     [ 0. ,  0. ]], 
    dtype=np.float32
)

X_ = np.array([[-0.28938353,  0.20824635],
       [ 0.3694414 , -0.2658577 ],
       [ 0.09482082, -0.06823505],
       [-0.1046629 ,  0.07531762],
       [ 0.        ,  0.        ]], dtype=np.float32)


plt.plot(X[:, 0], X[:, 1], "r^", X_[:, 0], X_[:, 1], "bs")
plt.show()
