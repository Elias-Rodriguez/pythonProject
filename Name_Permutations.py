# Write a program that lists all ways people can line up for a photo
# (all permutations of a list of strings). The program will read a list of one word names,
# then use a recursive method to create and output all possible orderings of those names, one ordering per line.

def all_permutations(permList, nameList):
    size = len(nameList)

    if size == 0:
        for i in range(len(permList)):
            print(permList[i], end=' ')
        print()
    else:
        for i in range(size):
            newPerms = permList.copy()
            newPerms.append(nameList[i])
            newNames = nameList.copy()
            newNames.pop(i)
            all_permutations(newPerms, newNames)


if __name__ == "__main__":
    nameList = input("Type in some names:").split(' ')
    permList = []
    all_permutations(permList, nameList)