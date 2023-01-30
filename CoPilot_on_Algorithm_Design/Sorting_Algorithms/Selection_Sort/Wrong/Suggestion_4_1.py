import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="" "")
            temp = temp.next


def insertion_sort(head):
    if head is None:
        return None
    sorted_list = Node(head.data)
    head = head.next
    while head:
        new_node = Node(head.data)
        temp = sorted_list
        while temp.next and temp.next.data < new_node.data:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        head = head.next
    return sorted_list

