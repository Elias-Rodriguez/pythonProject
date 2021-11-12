# Given a list of 10 names, complete the program that outputs the name specified
# by the list index entered by the user. Use a try block to output the name and an
# except block to catch any IndexError. Output the message from the exception object
# if an IndexError is caught. Output the first element in the list if the invalid
# index is negative or the last element if the invalid index is positive.

names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']


# Type your code here.
try:
    index = int(input("Type in place:"))
    print('Name: {}'.format(names[index]))
except IndexError as excpt:
    print('Exception! {}'.format(excpt))
    if index < 0:
        print("The closest name is: {}".format(names[0]))
    else:
        print("The closest name is: {}".format(names[len(names)-1]))