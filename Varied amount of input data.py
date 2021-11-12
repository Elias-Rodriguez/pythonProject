# 1) 8.16 LAB: Varied amount of input data
# Statistics are often calculated with varying
# amounts of input data. Write a program that takes
# any number of integers as input, and outputs the average and max.

list_of_num = input().split()
list_of_num = [int(x) for x in list_of_num]
list_of_num.sort()
list_of_num_int = map(int, list_of_num[::])

max_num = max(list_of_num)


def average_of_list(num):
    sum_of_num = 0
    for i in num:
        sum_of_num += i
    average = sum_of_num / len(list_of_num)
    return average


print('{} {}'.format(int(average_of_list(list_of_num_int)), max_num))
