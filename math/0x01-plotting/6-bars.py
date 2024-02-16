#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

names = ["Farrah", "Fred", "Felicia"]
fruits_names = ["apples", "bananas", "oranges", "peaches"]
fruits_colors = ["red", "yellow", "#ff8000", "#ffe5b4"]

for i in range(len(fruit)):
    bottom = 0
    for j in range(i):
        bottom += fruit[j]
    plt.bar(np.arange(len(names)),
            height=fruit[i],
            width=0.5,
            bottom=bottom,
            color=fruits_colors[i],
            label=fruits_names[i])

plt.ylim([0, 80])
plt.yticks(np.arange(0, 81, step=10))
plt.xticks(np.arange(len(names)), names)

plt.title("Number of Fruit per Person")
plt.ylabel("Quantity of Fruit")
plt.legend()

plt.show()
