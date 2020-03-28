import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,40,100) # List of evenly spaced numbers over the range
plt.plot(x, np.sin(x)) # plot sine of each x point
plt.show()
