import re


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    def print_list(self):

        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

    def push(self, new_data, prev=None, next=None):

        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        elif prev is None:
            self.head = new_node
            new_node.next = next
        elif next is None:
            prev.next = new_node
        else:
            prev.next = new_node
            new_node.next = next

    def search(self, x):

        # Initialize current to head
        current = self.head

        # loop till current not equal to None
        while current is not None:
            if current.data[0] == x:
                return current  # data found

            current = current.next

        return False  # Data Not found

    def position(self, key):
        current = self.head
        while current is not None:
            if current.next is None:
                if current.data[0] < key:
                    return current, None
                else:
                    return None, current
            if current.data[0] < key < current.next.data[0]:
                return current, current.next
            else:
                current = current.next

    def delete(self, key):
        current = self.head
        while current is not None:
            if current.next.next is None and current.next.data[0] == key:
                current.next = None
                return True
            elif current.next is None and current.data[0] == key:
                self.head = None
                return True
            elif current.next.data[0] == key:
                current.next = current.next.next
                return True
            elif current.data[0] == key:
                self.head = current.next
                return True
            else:
                current = current.next

    def search_with_regex(self, regex):
        current = self.head
        search_result = []

        while current is not None:
            if re.search(regex, current.data[0]).span()[1]:
                search_result.append(current)
            current = current.next

        return search_result

    @staticmethod
    def update(node, new_data):

        key = node.data[0]
        if key != new_data[0]:
            return False
        else:
            node.data = new_data
