import matplotlib.pyplot as plt
import numpy as np

# Membuat plotting sederhana

x = [1, 2, 3, 4]
y = [1, 4, 2, 3]


fig, ax = plt.subplots() # Membuat sebuah figure dan sebuah axes
ax.plot(x, y) # melakukan plotting data pada axes
plt.show()

fig, axs = plt.subplots() # Multiple subplot
plt.show()

# OBJECT ORIENTED STYLE
a = np.linspace(0, 2, 100)

fig, ax = plt.subplots()
# plotting tiga variant data pada axes
ax.plot(a, a, label='linear')
ax.plot(a, a**2, label='quadratic')
ax.plot(a, a**3, label='cubic')

# menyertakan label pada axes
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple Plot")
ax.legend()

plt.show()

# PYPLOT STYLE
plt.plot(a, a, label='linear')
plt.plot(a, a**2, label='quadratic')
plt.plot(a, a**3, label='cubic')

# menyertakan label pada axes
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

plt.show()