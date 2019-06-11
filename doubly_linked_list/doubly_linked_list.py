"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is pointing to."""
  
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is pointing to."""
  
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    # add_to_head replaces the head of the list with a new value that is passed in.
    if not self.head:
        self.head = ListNode(value)
        self.tail = self.head
    else:
        self.head.insert_before(value)
        self.head = self.head.prev
    
    self.length += 1

  def remove_from_head(self):
    # remove_from_head removes the head node and returns the value stored in it.
    temp = 0
    if self.length > 0:
      temp = self.head.value
      if self.head == self.tail:
        self.head = None
        self.tail = None
    else:
      self.head.delete()

    self.length -= 1
    return temp


  def add_to_tail(self, value):
    # add_to_tail replaces the tail of the list with a new value that is passed in.
    if not self.tail:
        self.tail = ListNode(value)
        self.head = self.tail
    else:
        self.tail.insert_after(value)
        self.tail = self.tail.next
    
    self.length += 1

  def remove_from_tail(self):
    # remove_from_tail removes the tail node and returns the value stored in it.
    temp = 0
    if self.length > 0:
      temp = self.tail.value
      if self.head == self.tail:
        self.head = None
        self.tail = None
    else:
      self.tail.delete()

    self.length -= 1
    return temp

  def move_to_front(self, node):
    # move_to_front takes a reference to a node in the list and moves it to the front of the list, 
    # shifting all other list nodes down.
    if self.head is not node:
        if node.next and node.prev:
            node.delete()
        current_head = self.head
        self.head = node
        node.next = current_head
        current_head.prev = node
    
    self.length += 0

  def move_to_end(self, node):
    # move_to_end takes a reference to a node in the list and moves it to the end of the list, 
    # shifting all other list nodes up.
    if self.tail is not node:
      if node.next and node.prev:
          node.delete()
      current_tail = self.tail
      self.tail = node
      node.prev = current_tail
      current_tail.next = node
    
    self.length += 0

  def delete(self, node):
    # delete takes a reference to a node in the list and removes it from the list. 
    # The deleted node's previous and next pointers should point to each afterwards.
    if node.next is None and node.prev is not None:
        node.prev.next = None
        self.tail = node.prev
        return node.value
    if node.prev is None and node.next is not None:
        node.next.prev = None
        self.head = node.next
        return node.value
    if node.prev is None and node.next is None:
        self.head = None
        self.tail = None
        return node.value
    else:
        node.delete()
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
    
    # self.length -= 1
    # return node.value
    
  def get_max(self):
    # get_max returns the maximum value in the list.
    pass
