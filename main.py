from linked_list import MyList, ListNode

lst = MyList()

nd = ListNode(1)
lst.add(nd)
nd = ListNode(2)
lst.add(nd)
nd = ListNode(3)
lst.add(nd)
lst.remove(2)
#lst.remove(1)

for data in lst:
   print(data)
