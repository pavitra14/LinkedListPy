import copy

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  def __str__(self):
    return "Node[]: {}".format(self.data)

class LinkedList:
  def __init__(self, data):
    self.head = Node(data)
    self.tail = None
  
  def getHead(self):
    return self.head
  
  def setHead(self, head):
    self.head = head

  def insert(self, data):
    node = Node(data)
    head = self.head
    if head.data is None:
      head.data = data
      return
    ptr = head
    while ptr.next != None:
      ptr = ptr.next
    ptr.next = node
  
  def insert_at_start(self, data):
    node = Node(data)
    node.next = self.head
    self.head = node

  def insert_at_index(self, index, data):
    head = self.head
    if head.data is None:
      head.data = data
      return
    
    if index == 0:
      self.insert_at_start(data)
      return
    
    i = 0
    ptr = head
    while i + 1 != index :
      ptr = ptr.next
      if ptr == None:
        raise Exception("Limit of Linked List Exceeded: Overflow")
        return
      i+=1
    node = Node(data)
    temp = ptr.next
    ptr.next = node
    node.next = temp
  
  def display(self):
    ptr = copy.copy(self.head)
    ans = []
    while ptr:
      ans.append(str(ptr.data))
      ptr = ptr.next
    print("->".join(ans))

  def reverse(self):
    prev = None
    current = self.head
    while (current is not None):
      n = current.next
      current.next = prev
      prev = current
      current = n
    self.head = prev


Link = LinkedList(1)
for _ in range(2,11):
  Link.insert(_)

Link.display()

Link.reverse()

Link.display()

Link.reverse()

Link.display()