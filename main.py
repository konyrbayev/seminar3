from linked_list import MyList, ListNode
from myclass import Shape

sh1=Shape(3,1)
sh2=Shape(5,7)
sh3=Shape(4,2)
sh4=Shape()
l=MyList()
l.push(sh1)
l.push(sh2)
l.push(sh3)
l.push(sh4)

print("After adding objects: ")
for i in l:
   i.define()

print("\nAfter popping last object: ")
l.pop()
for i in l:
   i.define()

print("\nAfter popping last object: ")
l.pop()
for i in l:
   i.define()


