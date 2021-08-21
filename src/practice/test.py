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
           new_node= Node(data)
           new_node.next_value=self.head_node
           self.head_node=new_node
            

    def print(self):
        current_node = self.head_node
        while(current_node is not None):
            print(current_node.data)
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
            previous_node = None
            while(current_node is not None):

                if(current_node.data == value):
                    previous_node.next_value = current_node.next_value
                    break
                previous_node = current_node
                current_node = current_node.next_value


linked_list = SinglyLinkedList()
for i in range(1, 6, 1):
    linked_list.inset_at_first(i)


linked_list.is_empty()
linked_list.print()
linked_list.remove_by_value(2)
linked_list.print()
linked_list.remove()
