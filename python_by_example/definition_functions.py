import matplotlib.pyplot as plt
import numpy as np


def generate_data(n):
    e_values = []
    for i in range(n):
        e = np.random.randn()
        e_values.append(e)
    return e_values


data = generate_data(300)
plt.plot(data)
plt.show()
