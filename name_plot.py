import matplotlib.pyplot as plt
import numpy as np

# Letter E

stem_of_E = [1, 2, 3, 4, 5]
line_one_of_E = [1, 2, 3]
line_two_of_E = [1, 2]
line_three_of_E = [1, 2, 3]

plt.plot([1,1,1,1,1], stem_of_E)
plt.plot(line_one_of_E, [5,5,5])
plt.plot(line_three_of_E, [1,1,1])
plt.plot(line_two_of_E, [3,3])

# LSetter L

stem_of_l = [1, 2, 3, 4, 5]
base_of_l = [1,1,1]

plt.plot([5,5,5,5,5], stem_of_l)
plt.plot([5,6,7], base_of_l)

# Letter I
body_of_i = [1, 2, 3, 4, 5]
bottom_line_of_i = [1,1,1]
top_line_of_i =[5,5,5]


plt.plot([10,10,10,10,10 ], body_of_i)
plt.plot([9,10,11], bottom_line_of_i)
plt.plot([9,10,11], top_line_of_i)

# Letter A

frame_of_a = [1,5,1]
line_of_a = [3,3]

plt.plot([13,14,15], frame_of_a)
plt.plot([13.5,14.5], line_of_a)


# Letter S

top_line_of_s = top_line_of_i
bottom_line_of_s = bottom_line_of_i
middle_line_of_s = [3, 3, 3]
first_line_of_s = [5,3]
second_line_of_s = [3,1]

plt.plot([17,18,19], top_line_of_s)
plt.plot([17,18,19], bottom_line_of_s)
plt.plot([17,18,19], middle_line_of_s)
plt.plot([17,17],first_line_of_s)
plt.plot([19,19], second_line_of_s)


# Show my Plotted name ELIAS
plt.title('The Name "ELIAS" Plotted')
plt.show()
