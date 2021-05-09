class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        # 비어있는 경우
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        # 비어있지 않는 경우
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data, prev=node)
            node.next = new
            self.tail = new

    def insert_before(self, next_data, new_data):
        # when node is empty
        if self.head is None:
            self.head = Node(new_data)
            self.tail = self.head
            return True
        else:
            node = self.tail
            while node.data != next_data:
                node = node.prev
                # target.prev should be present
                if not node:
                    return False
            prev_node = node.prev
            new_node = Node(new_data, next=node, prev=prev_node)
            if prev_node:
                prev_node.next = new_node
            node.prev = new_node
            return True

    def insert_after(self, prev_data, new_data):
        if not self.head:
            self.head = Node(new_data)
            self.tail = self.head
            return True
        else:
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
            return True

        # # empty state
        # if not self.head:
        #     self.head = Node(new_data)
        #     self.tail = self.head
        #     return True
        # # not empty state : one or more exist
        # else:
        #     node = self.head
        #     # prev_data (: 새로운 노드를 생성할 떄, 어떤값 다음에 넣을지에 대한 정보 )가 현재 node와 같은지 비교
        #     while prev_data != node.data:
        #         node = node.next
        #         if not node:
        #             return False

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


if __name__ == '__main__':
    pass
