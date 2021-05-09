class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.del_list = []

    def insert(self, data):
        # 비어있는 경우
        node = self.head
        while node.next:
            node = node.next
        new = Node(data, prev=node)
        node.next = new
        self.tail = new

    def insert_after(self, prev_data, new_data):

        node = self.head
        while node.data != prev_data:
            node = node.next
            if not node:
                return False

        next_node = node.next
        new_node = Node(new_data, next=next_node, prev=node)

        if next_node:
            next_node.prev = new_node
        node.next = new_node

    def moveCurrentUpward(self, l):
        for _ in range(l):
            self.head = self.head.prev

    def moveCurrentDownward(self, l):
        # node = self.head
        for _ in range(l):
            self.head = self.head.next

    def deleteOut(self, node):
        if not self.head:
            return -1

        temp = self.head.data

        front = node.prev
        rear = node.next
        #
        # if node.prev and node.next:
        #     front.next = rear
        #     rear.prev = front
        if not front:

            rear.prev = None
        elif not rear:
            front.next = None

        else:
            front.next = rear
            rear.prev = front

        if self.head.next:
            self.head = self.head.next

        else:
            self.head = self.head.prev

        return temp


def solution(n, k, cmd):
    answer = ['O'] * n

    doubly_linked_list = DoublyLinkedList(0)
    for i in range(1, n):
        doubly_linked_list.insert(i)
    doubly_linked_list.moveCurrentDownward(k)

    # current_data = doubly_linked_list.head.data
    # print(current_data)

    deleted_stack = []

    for command in cmd:

        if command[0] == 'D':
            doubly_linked_list.moveCurrentDownward(int(command[-1]))
        elif command[0] == 'U':
            doubly_linked_list.moveCurrentUpward(int(command[-1]))
        elif command[0] == 'C':
            deleted_stack.append(doubly_linked_list.deleteOut(doubly_linked_list.head))
        else:
            prev_val = deleted_stack[-1] - 1
            doubly_linked_list.insert_after(prev_data=prev_val, new_data=deleted_stack.pop())

    # print('current_head_data', doubly_linked_list.head.data)

    while deleted_stack:
        answer[deleted_stack.pop()] = 'X'

    return "".join(answer)


if __name__ == '__main__':
    n = 8
    k = 2
    cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
    # OOOOXOOO
    cmd_2 = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
    # OOXOXOOO
    print(solution(n, k, cmd))
    # l = ['O' * 8]
    # l[4] = 'x'
    # print(l)
