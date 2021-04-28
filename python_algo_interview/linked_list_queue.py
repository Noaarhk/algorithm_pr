# Linked List 를 이용해서 구현

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    '''
    1. 기존의 선형연결리스트는 하나의 포인터만 사용하여 헤드를 가리켰지만 테일을 가리키는 포이터를 하나 추가 하면 간단히 해결된다.
    '''

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, node):

        # 큐가 비어있을때 노드하나가 추가되면 헤드와 테일이 같은 노드를 가리킨다.
        if not self.head:
            self.head = node
            self.tail = node
        # 큐가 비어있지 않을 때 테일뒤에 새로운 노드를 연결시킨다. 그리고 포인터(테일에서 테일의 넥스트로) 의 위치를 추가된 테일로 옮긴다.
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def dequeue(self):
        # 큐가 비어있는 경우
        if not self.head:
            return -1
        # 제거할 요소를 임시로 가지고있는다.
        temp = self.head.data
        # 제거한 후의 헤드로 기존의 포인터를 옮긴다.
        self.head = self.head.next

        # 큐에 하나만 있어서 제거 후에 비어있는 경우
        if not self.head:
            # 테일도 헤드와 같이 빈공간을 가리킨다.
            self.tail = None

        return temp

    def print(self):
        curr_node = self.head
        string = ""
        while curr_node:
            string += str(curr_node.data)
            if curr_node.next:
                string += "->"
            curr_node = curr_node.next
        print(string)


if __name__ == '__main__':
    s = SinglyLinkedList()
    s.enqueue(Node(1))
    s.enqueue(Node(2))
    s.enqueue(Node(3))
    s.enqueue(Node(4))
    s.print()

    print(s.dequeue())
    print(s.dequeue())
    s.print()
    print(s.dequeue())
    print(s.dequeue())
    s.print()
