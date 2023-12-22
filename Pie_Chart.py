import matplotlib.pyplot as plt
import numpy as np
language= ["C++", 'Java' ,"Python", "Go", "C#" ]
votes= [11, 34, 17, 29, 12]
explodes= [0, 0, 0.5, 0,0]
# plt.pie(votes, labels=language)
plt.pie(votes, labels=language, explode=explodes)
plt.show()