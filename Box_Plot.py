import matplotlib.pyplot as plt
import numpy as np
height= np.random.normal(171, 38, 300)
plt.boxplot(height)
plt.show()

# a= np.arange(1, 100).reshape(11,9)
# print(a)