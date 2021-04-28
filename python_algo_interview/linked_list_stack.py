from typing import List


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        self.head = Node(data, self.head)

    def toLinkedStack(self, nums: List):
        head = Node(None)
        for val in nums:
            node = Node(val)
            head.next = node
            head = node

        print(head.data)

    def pop(self):
        temp = self.head
        self.head = self.head.next
        return temp


# 리스트를 받아 연결리스트로 변환
def toLinkedList(nums: List):
    head = Node(nums[0])
    itr = head

    for i in nums[1:]:
        node = Node(i)
        itr.next = node
        itr = node


def printLinkedList(nums: Node):
    itr = nums
    while itr:
        print(itr.data)
        itr = itr.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    linked_list = toLinkedList(nums)
    # printLinkedList(linked_list)

    stack = Stack()
    stack.toLinkedStack(nums)

    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # stack.push(4)
    # stack.pop()
    #
    # print(stack.head.data)
