'''
定义并实现随机单链表，并重写append方法，添加随机指针，重写display方法，打印随机指针。
构建随机单链表，并打印结果。
利用字典记录两链表节点对应关系，实现拷贝上述构建的随机单链表，并打印结果。
'''
import random
from chapter07eg01cyclelink import LinkedList, ListNode
class RandomLinkNode(ListNode):#随机单链节点定义
    def __init__(self, value=0, next=None,random_next=None):
        super().__init__(value, next)
        self.random_next = random_next
class RandomLinkedList(LinkedList):#随机单链表定义
    def append(self, value):#重写append方法，添加随机指针
        if not self.head:
            self.head = RandomLinkNode(value)
        else:
            current = self.head
            node_set = [current]
            while current.next:
                current = current.next
                node_set.append(current)
            node=RandomLinkNode(value)
            current.next = node
            node_set.append(node)
            node.random_next = random.choice(node_set+[None])
    def display(self):#重写display方法，打印随机指针
        head = self.head
        while head:
            print(
                f"{head.value}({head.random_next.value if head.random_next else 'None'})",
                end='->')
            head = head.next
        print('None')
#构建随机单链表
random_link = RandomLinkedList()
for i in range(10):
    random_link.append(i)
random_link.display()
#利用字典记录两链表节点对应关系，实现拷贝random_link(上述构建的随机单链表),并打印结果
copy_random_link = RandomLinkedList()
copy_random_link.head = RandomLinkNode(random_link.head.value)
new_node=copy_random_link.head
current = random_link.head
dict_node = {current:new_node}
while current:
    if current.next:
        if current.next not in dict_node:
            new_node.next = RandomLinkNode(current.next.value)
            dict_node[current.next] = new_node.next
        else:
            new_node.next = dict_node[current.next]
    if current.random_next:
        if current.random_next not in dict_node:
            new_node.random_next = RandomLinkNode(current.random_next.value)
            dict_node[current.random_next] = new_node.random_next
        else:
            new_node.random_next = dict_node[current.random_next]
    new_node = new_node.next
    current = current.next

copy_random_link.display()
