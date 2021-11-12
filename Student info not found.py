# Given a main program that searches for the ID or the name of a
# student from a dictionary, complete the find_ID() and the find_name()
# functions that return the corresponding information of a student. Then,
# insert a try/except statement in main() to catch any exceptions thrown by find_ID()
# or find_name(), and output the exception message. Each entry of the dictionary
# contains the name (key) and the ID (value) of a student.




# Define custom exception
class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message  # Initialize the exception message


def find_ID(name, info):
    # Type your code here.
    if name in info:
        return info[name]
    raise StudentInfoError("Student ID not found for " + name)


def find_name(ID, info):
    for name in info:
        if ID == info[name]:
            return name
    raise StudentInfoError("Student name not found for " + ID)


if __name__ == '__main__':
    # Dictionary of student names and IDs
    student_info = {
        'Reagan': 'rebradshaw835',
        'Ryley': 'rbarber894',
        'Peyton': 'pstott885',
        'Tyrese': 'tmayo945',
        'Caius': 'ccharlton329'
    }

    userChoice = input("Type 0 for search by name or 1 to search by ID:")  # Read search option from user. 0: find_ID(), 1: find_name()

    # FIXME: find_ID() and find_name() may throw an Exception.
    #        Insert a try/except statement to catch the exception and output any exception message.
    try:
        if userChoice == "0":
            name = input("Type in name:")
            result = find_ID(name, student_info)
        else:
            ID = input("Type in ID:")
            result = find_name(ID, student_info)
        print(result)
    except StudentInfoError as excpt:
        print(excpt)