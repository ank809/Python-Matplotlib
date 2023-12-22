import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
language= ["C++", 'Java' ,"Python", "Go", "C#" ]
votes= [11, 34, 17, 29, 12]
# Styling
style.use("dark_background")
plt.pie(votes, labels=None)
plt.legend(language)
plt.show()