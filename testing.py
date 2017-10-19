import matplotlib.pyplot as plt
import math
from math import *
x=[i*0.1 for i in range(100)]
y=[sin(t)for t in x]
plt.plot(x,y,label='sin(x)')
plt.legend()
