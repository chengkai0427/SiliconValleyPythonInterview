from chapter07eg01cyclelink import LinkedList
link=LinkedList()
for i in range(1,6):
    link.append(i)
link.display()
prev,current=None,link.head
while current:
    current.next,prev,current=prev,current,current.next
link.head=prev
link.display()