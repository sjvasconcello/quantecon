import matplotlib.pyplot as plt
import numpy as np


def generate_data(n, generator_type):
    e_values = []
    for i in range(n):
        e = generator_type()
        e_values.append(e)
    return e_values

data = generate_data(100, np.random.uniform)
plt.plot(data)
plt.show()
