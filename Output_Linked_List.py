# Write a recursive function called print_list() that outputs the integer value of each node in
# a linked list. Function print_list() has one parameter, the head node of a list. The main program
# reads the size of the linked list, followed by the values in the list. Assume the linked list has at least 1 node.

class Node:
    def __init__(self, value):
        self.data_val = value
        self.next_node = None

    def insert_after(self, node):
        tmp_node = self.next_node
        self.next_node = node
        node.next_node = tmp_node

    def get_next(self):
        return self.next_node

    def print_data(self):
        print(self.data_val, end=", ")


# TODO: Write recursive print_list() function here.
def print_list(node):
    if node != None:
        node.print_data()
        print_list(node.get_next())


if __name__ == "__main__":
    size = int(input("Type in the size of list:"))
    value = int(input("Type in the values:"))
    head_node = Node(value)  # Make head node as the first node
    last_node = head_node

    # Insert the second and the rest of the nodes
    for n in range(1, size):
        value = int(input("Type in the values:"))
        new_node = Node(value)
        last_node.insert_after(new_node)
        last_node = new_node

    print_list(head_node)
