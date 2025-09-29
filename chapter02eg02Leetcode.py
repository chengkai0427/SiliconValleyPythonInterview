import re

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class NodeList:
    def __init__(self):
        self.head = None
    def add(self, val):
        if not self.head:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
    def printList(self):
        curr = self.head
        while curr:
            if curr.next:
                print(curr.val, end='->')
            else:
                print(curr.val)
            curr = curr.next
    def listToInt(self)->int:
        curr = self.head
        sumlist = self.head.val
        while curr.next:
            sumlist = sumlist*10 + curr.next.val
            curr = curr.next
        return sumlist

class Leetcode:
    def __init__(self,l1: NodeList, l2: NodeList):
        self.l1 = l1
        self.l2 = l2
    def addTwo(self) -> NodeList:
        l3 = NodeList()
        for c in str(self.l1.listToInt() + self.l2.listToInt()):
            l3.add(int(c))
        return l3

numlist1=input('请输入第一个数字的链条，用->连接，如：7->2->4->3：')
list1=NodeList()
if re.match(r'^\d(->\d)*$', numlist1):
    for v in re.findall(r'\d', numlist1):
        list1.add(int(v))
else:
    raise ValueError('输入格式错误')
numlist2=input('请输入第二个数字的链条，用->连接，如：7->2->4->3：')
list2=NodeList()
if re.match(r'^\d(->\d)*$', numlist2):
    for v in re.findall(r'\d', numlist2):
        list2.add(int(v))
else:
    raise ValueError('输入格式错误')

leetcode=Leetcode(list1,list2)
result=leetcode.addTwo()
result.printList()