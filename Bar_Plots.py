import matplotlib.pyplot as plt
import numpy as np
language= ["C++", 'Java' ,"Python", "Go", "C" ]
votes= [21, 34, 27, 33, 12]
# plt.bar(language, votes)
plt.bar(language, votes, color="Green", align="edge", width= 0.5, edgecolor="Red") # by default the graph starts in mid of C++
plt.xlabel("Language")  # if you want the bar start from C++ the use edge

# plt.barh(language, votes) plots the bar horizontally
plt.ylabel("Votes")
plt.show()