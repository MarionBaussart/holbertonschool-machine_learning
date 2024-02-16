#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(y, color='red', linestyle='solid')  # or plt.plot(y, 'r-')
plt.xlim([0, 10])

plt.show()
