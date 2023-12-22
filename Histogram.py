# A histogram is a graph showing frequency distributions.
import matplotlib.pyplot as plt
import numpy as np

x= np.random.normal(30, 45, 1000) # (mean s.d, size)
print(x)

plt.hist(x)
plt.show()