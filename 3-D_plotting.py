import  matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
ax= plt.axes(projection="3d")
x= np.random.random(100)
y= np.random.random(100)
z= np.random.random(100)
ax.scatter(x,y,z)
ax.set_title("3-D plot")
plt.show()