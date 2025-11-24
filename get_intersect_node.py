'''先构建两个单链表，然后将其中一个单链表的尾节点指向另一个单链表的随机节点，最后找出找两个单链表的交点'''
import random
from chapter07eg01cyclelink import LinkedList
llist1 = LinkedList()
llist2 = LinkedList()
for i in range(random.randint(1,15)):
    llist1.append(i)
for i in range(random.randint(1,10)):
    llist2.append(i)
inter_node = llist1.head
for i in range(random.randint(1,10)):
    inter_node = inter_node.next
tail = llist2.head
while tail.next:
    tail = tail.next
tail.next = inter_node
list1_node_set = set()
head1 = llist1.head
while head1:
    list1_node_set.add(head1)
    head1 = head1.next
head2 = llist2.head
while head2:
    if head2 in list1_node_set:
        print(f"Intersection node is:{head2}，value is:{head2.value}")
        break
    else:
        head2 = head2.next
if not head2:
    print(f"No intersection node found")