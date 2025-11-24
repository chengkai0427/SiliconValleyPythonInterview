'''
首先实现一个单链表类，包括append、prepend、delete、display、cycle_detection（检测是否有环）五个方法。
然后测试，并随机选择一个节点作为循环节点，将尾节点的next指针指向循环节点，检测链表是否循环，无循环则直接调用display()，
有循环则重新定义打印方式并将循环节点用括号括起来。
'''
class ListNode:#节点定义
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:#单链表定义
    def __init__(self):
        self.head = None

    def append(self, value):#在尾部添加节点
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def prepend(self, value):#在前面添加节点
        self.head = ListNode(value, self.head)

    def delete(self, value):#删除节点
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def display(self):#非循环链接打印
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def cycle_detection(self):#检测链表是否循环
        if not self.head:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#测试
if __name__ == '__main__':
    import random
    #创建空单链表
    llist = LinkedList()
    #添加10个节点
    for i in range(10):
        llist.append(i)
    #随机选择一个节点作为循环节点
    cycle_node = llist.head
    for i in range(random.randint(1, 10)):
        cycle_node = cycle_node.next
    #找到尾节点
    tail = llist.head
    while tail.next:
        tail = tail.next
    #将尾节点的next指针指向循环节点
    tail.next = cycle_node
    #检测链表是否循环，无循环则直接调用display()，有循环则重新定义打印方式并将循环节点用括号括起来
    if llist.cycle_detection():
        head = llist.head
        cycle=0
        while cycle<2:
            print(head.value, end=" -> ")
            head = head.next
            if head == cycle_node:
                cycle+=1
        print(f"({head.value})")
    else:
        llist.display()