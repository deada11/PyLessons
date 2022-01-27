import numpy as np

x = np.arange(1, 101)

data = x[(x % 5 == 0) & (x % 3 == 0)]
print(data)

