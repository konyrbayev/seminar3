from mylistiterator import MyListIterator
from myclass import Shape
class ListNode:
  def __init__(self, data=None):
      self.data = data 
      self.next = None
 
class MyList:
  def __init__(self):
    self.head = None

  def push(self, data):
    if self.head is None:
      self.head = ListNode(data)
    else:
      new_node = ListNode(data)
      new_node.next = self.head
      self.head = new_node
 
  def pop(self):
    if self.head is None:
      return None
    else:
      popped = self.head.data
      self.head = self.head.next
      return popped

  def len( self ):
    return self.size

  def __contains__(self,target):
    curNode = self.head
    while (curNode is not None) and \
      (curNode.data!=target):
        curNode = curNode.next
        return curNode is not None

  def search( self, target ):
    curNode = self.head
    while (curNode is not None) and \
      (curNode.data!=target):
      curNode = curNode.next
      return curNode 

  def __iter__( self ):
      return MyListIterator(self.head)



