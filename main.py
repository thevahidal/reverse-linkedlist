class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, value):
        node = Node(value)

        tmp = self.head
        while tmp.next != None:
            tmp = tmp.next

        tmp.next = node
        return node

    def display(self):
        result = []

        tmp = self.head
        while tmp.next != None:
            tmp = tmp.next
            result.append(tmp.value)
        print(result)

    def length(self):
        counter = 0

        tmp = self.head
        while tmp.next != None:
            tmp = tmp.next
            counter += 1

        return counter

    def get(self, index):
        counter = 0

        tmp = self.head
        while counter == index:
            tmp = tmp.next
            counter += 1

        return tmp.value

    def remove(self, index):
        counter = 0

        tmp = self.head
        while counter < index:
            tmp = tmp.next
            counter += 1

        removed = tmp.next    
        tmp.next = removed.next

        return removed.value

    # def reverse(self):
    #     tmp = self.head
    #     while tmp.next != None:
    #         tmp.next = tmp 
    #         tmp = tmp.next
    #     self.head = tmp
        

ll = LinkedList()
ll.append(124)
ll.append(0)
ll.append(57)
ll.append(-10)
ll.append(3)
ll.append(67)
ll.append(8)
ll.append(-36)
ll.append(-130)

ll.display()
