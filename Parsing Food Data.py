# Type your code here
column1 = []
column2 = []
column3 = []
column4 = []

input_file_name = input("Type in the text file name:")
f = open(input_file_name)

for row in f:
    fields = row[:-1].split('\t')  # -1 to omit final newline
    column1.append(fields[0])
    column2.append(fields[1])
    column3.append(fields[2])
    column4.append(fields[3])

for rowNum in range(len(column4)):
    if column4[rowNum] == "Available":
        print(column2[rowNum] + " (" + column1[rowNum] + ") -- " + column3[rowNum])
