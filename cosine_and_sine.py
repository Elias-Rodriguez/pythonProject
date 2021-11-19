# https://matplotlib.org/stable/tutorials/introductory/pyplot.html

import matplotlib.pyplot as plt
import numpy as np

x_value = np.arange(0, 4 * np.pi, 0.1)
cosine_wave = np.cos(x_value)
sine_wave = np.sin(x_value)

plt.scatter(x_value, sine_wave, s =80, facecolors = 'none', edgecolors='b')
plt.scatter(x_value, cosine_wave, color = 'green', marker = 'x')

plt.xlabel('x values from 0 to 4pi')
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.legend(['sin(x)', 'cos(x)'])

plt.show()
