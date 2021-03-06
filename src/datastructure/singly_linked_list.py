class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_value = None


class SinglyLinkedList:
    def __init__(self):
        self.head_node = None

    def is_empty(self):
        if(self.head_node is None):
            return True
        else:
            return False

    def inset_at_first(self, data):
        if(self.is_empty()):
            new_node = Node(data)
            self.head_node = new_node
        else:
            new_node = Node(data)
            new_node.next_value = self.head_node
            self.head_node = new_node

    def inset_at_last(self, data):
        if (self.is_empty()):
            new_node = Node(data)
            self.head_node = new_node
        else:
            last_node = self.head_node
            while(last_node.next_value is not None):
                last_node = last_node.next_value
            new_node = Node(data)
            last_node.next_value = new_node

    def list(self):
        current_node = self.head_node
        while(current_node is not None):
            print(current_node.data, end=" ")
            current_node = current_node.next_value

    def remove(self):
        if(self.is_empty()):
            print("list empty")
        else:
            self.head_node = None
            print("removed")

    def remove_by_value(self, value):
        if(self.is_empty()):
            print("list empty")
        else:
            current_node = self.head_node
            previous_node = current_node

            while(current_node is not None):
                if(current_node.data == value and current_node == previous_node):
                    self.head_node = current_node.next_value
                    break
                elif(current_node.data == value):
                    previous_node.next_value = current_node.next_value
                    current_node=None
                    break
                previous_node = current_node
                current_node = current_node.next_value


linked_list = SinglyLinkedList()
for i in range(1, 6, 1):
    linked_list.inset_at_first(i)

for i in range(10, 16, 1):
    linked_list.inset_at_last(i)


linked_list.remove_by_value(12)
linked_list.list()
