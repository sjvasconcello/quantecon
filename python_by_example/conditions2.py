import matplotlib.pyplot as plt
import numpy as np


def generate_data(n, generator_type):
    e_values = []
    for i in range(n):
        if generator_type == 'U':
            e = np.random.uniform(0, 1)
        else:
            e = np.random.randn()
        e_values.append(e)
    return e_values


data = generate_data(100, 'U')
plt.plot(data)
plt.show()
