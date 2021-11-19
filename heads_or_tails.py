import matplotlib.pyplot as plt
import random

y_values = []
x_values = []
times_flipped = 25

for number in range(1, times_flipped + 1):
    # 1 for heads and 0 for tails
    face_value = random.randint(0, 1)
    y_values.append(face_value)
    x_values.append(number)

plt.plot(x_values, y_values)
plt.show()

