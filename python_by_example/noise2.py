import matplotlib.pyplot as plt
import numpy as np

ts_length = 200
e_values = [] # Emply list

for i in range(ts_length):
  e = np.random.randn()
  e_values.append(e)

plt.plot(e_values)
plt.show()
