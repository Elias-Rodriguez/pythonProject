# Asks the user for input to set a title, collumn one header, and a collumn 2 header
data_title = input('Enter a title for the data:\n')
print('You entered: {}\n'.format(data_title))

column_one_header = input('Enter the column 1 header:\n')
print('You entered: {}\n'.format(column_one_header))

column_two_header = input('Enter the column 2 header:\n')
print('You entered: {}\n'.format(column_two_header))

# initiated two lists. One to keep track of authors and the other to keep track of
# the number of novels written by the authors.
authors = []
num_of_nov = []

# looping statemen to go through various inputs
while True:
    data_points = input('Enter a data point (-1 to stop input):\n')
    data = data_points.split(',')
    string = data[0]

    if data_points == '-1':
        print()
        break
    elif data_points.__contains__(',') == False:
        print('Error: No comma in string.\n')
        continue
    elif data_points.count(',') > 1:
        print('Error: Too many commas in input.\n')
        continue
    elif len(data) == 2 and data[1].replace(' ', '').isdigit() == False:
        print('Error: Comma not followed by an integer.\n')
        continue
    else:
        integer = int(data[1].replace(' ', ''))
        authors.append(string)
        num_of_nov.append(integer)
        print('Data string: {}'.format(string))
        print('Data integer: {}\n'.format(integer))
        continue

# print statements to populate a table with title , headings, authors, and number of novels
print('{name:>33}'.format(name=data_title))
print('{header1:<20}|{header2:>23}'.format(header1=column_one_header, header2=column_two_header))
print('-' * 44)
for (a, b) in zip(authors, num_of_nov):
    print('{:<20}|{:>23}'.format(a, b))

# different table to show authors and number of novels wrote displayed as asterix symbol
print()
for (a, b) in zip(authors, num_of_nov):
    print('{:>20} {:<}'.format(a, b * '*'))
