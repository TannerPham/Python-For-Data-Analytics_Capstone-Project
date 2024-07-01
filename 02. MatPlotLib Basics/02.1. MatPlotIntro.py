import matplotlib.pyplot as plt
import numpy as np
# how to create a simple line chart
x = np.arange(0,5,.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()