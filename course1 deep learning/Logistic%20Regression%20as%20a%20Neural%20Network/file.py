import numpy as np

a=np.random.randn(4,3)

print(a)

b=np.sum(a,axis=0,keepdims=True)

print(b)

