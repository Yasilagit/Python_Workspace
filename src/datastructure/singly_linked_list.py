# SinglyLinkedList
class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextValue = None


class SinglyLinkedList:
    def __init__(self):
        self.headValue = None


sList = SinglyLinkedList()
sList.headValue = Node("Sunday")
d2 = Node("Monday")
d3 = Node("Tueesday")
d4 = Node("Wednesday")
sList.headValue.nextValue = d2
d2.nextValue = d3
d3.nextValue = d4

currentHead = sList.headValue
while (currentHead is not None):
    print(currentHead.data)
    currentHead = currentHead.nextValue
