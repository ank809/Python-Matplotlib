import numpy as np
import matplotlib.pyplot as plt

# scatter() function to draw a scatter plot.
x= np.random.randint(1, 100, (10, 10))
print(x)
y= np.random.randint(1, 100, (10,10))
print(y)

# plt.scatter(x,y)
# plt.show()

x1= np.random.randint(1, 100, (10, 10))
print(x1)
y1= np.random.randint(1, 100, (10,10))
print(y1)
# plt.scatter(x1,y1)

# plt.show()

# Changing color of the plots
plt.scatter(x,y,color="pink")
plt.show()

# Color to single dots
x2 = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y2 = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x2, y2, c=colors, s=100, marker="*")

plt.show()