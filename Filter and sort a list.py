# 8.17 LAB: Filter and sort a list
# Write a program that gets a list of integers from input,
# and outputs non-negative integers in ascending order (lowest to highest).

list_of_num = input().split()
list_of_num = [int(x) for x in list_of_num]
list_of_num.sort()

list_num = []
for i in list_of_num:
    if i >= 0:
        list_num.append(i)


for i in list_num:
    print(i, end=' ')

