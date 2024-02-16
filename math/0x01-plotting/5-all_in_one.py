#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig = plt.figure()

fig.suptitle("All in One")

# Plot 0
ax0 = fig.add_subplot(3, 2, 1)
ax0.plot(y0, color='red', linestyle='solid')
ax0.set_xlim([0, 10])

# Plot 1: Men's Height vs Weight
ax1 = fig.add_subplot(3, 2, 2)
ax1.scatter(x1, y1, color="magenta")
ax1.set_title("Men's Height vs Weight", fontsize="x-small")
ax1.set_xlabel("Height (in)", fontsize="x-small")
ax1.set_ylabel("Weight (lbs)", fontsize="x-small")

# Plot 2: Exponential Decay of C-14
ax2 = fig.add_subplot(3, 2, 3)
ax2.plot(x2, y2, color="steelblue")
ax2.set_title("Exponential Decay of C-14", fontsize="x-small")
ax2.set_xlabel("Time (years)", fontsize="x-small")
ax2.set_ylabel("Fraction Remaining", fontsize="x-small")
ax2.set_xlim([0, 28650])
ax2.set_yscale("log")

# Plot 3: Exponential Decay of Radioactive Elements
ax3 = fig.add_subplot(3, 2, 4)
ax3.plot(x3, y31, color="red", linestyle="dashed", label="C-14")
ax3.plot(x3, y32, color="green", linestyle="solid", label="Ra-226")
ax3.set_title("Exponential Decay of Radioactive Elements", fontsize="x-small")
ax3.set_xlabel("Time (years)", fontsize="x-small")
ax3.set_ylabel("Fraction Remaining", fontsize="x-small")
ax3.set_xlim([0, 20000])
ax3.set_ylim([0, 1])
ax3.legend()

# Plot 4: Project A
ax4 = fig.add_subplot(3, 1, 3)
ax4.hist(student_grades, range=(0, 100), bins=10, color="steelblue",
         edgecolor="black")
ax4.set_title("Project A", fontsize="x-small")
ax4.set_xlabel("Grades", fontsize="x-small")
ax4.set_ylabel("Number of Students", fontsize="x-small")
ax4.set_xlim([0, 100])
ax4.set_ylim([0, 30])
ax4.set_xticks(np.arange(0, 101, step=10))

plt.tight_layout()
plt.show()
