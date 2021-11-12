import csv

# Type your code here.
file_name = input("Type in the file name:")
print("The output below will be the Number of times a word appeared(case sensitive) in the CSV file.")
word_list = []

with open(str(file_name), 'r') as csvfile:
    user_file = csv.reader(csvfile, delimiter=',')

    for row in user_file:
        for index in range(len(row)):
            if row[index] not in word_list:
                print('{} {}'.format(row[index], row.count(row[index])))
                word_list.append(row[index])