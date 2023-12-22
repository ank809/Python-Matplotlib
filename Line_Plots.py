import matplotlib.pyplot as plt
import numpy as np
year= [2006+x for x in range(16)]
weight=[86, 90,86, 69,54, 89, 90, 56 ,67, 78, 45, 67, 55, 43, 78,76]
# plt.plot(year, weight)
# plt.plot(year, weight, "r--")
plt.plot(year, weight, c= "Yellow", lw=3, linestyle= ":")  # --, -, -., :
plt.xlabel('Year')
plt.ylabel('Weights')
plt.title('Graph between Year and Weights')
plt.show()

y1= np.array([2,4,6,8])
y2= np.array([1,3,5,7])
plt.plot(y1, c="hotpink", lw=3)
plt.plot(y2, c="yellow", lw=3)
plt.show()