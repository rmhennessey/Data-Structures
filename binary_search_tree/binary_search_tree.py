class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # check if the new node's value is less than our current node's value
    if value < self.value:
      # if there's no left child here already, place the new node here
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        # otherwise, repeat the process!
        self.left.insert(value)
    # check if the new node's value is greater than or equal to our current node's value
    elif value >= self.value:
      # if there's no right child here already, place the new node here
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        # otherwise, repeat the process!
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    
    elif target < self.value:
      if not self.left:
      # can also do if self.left == None: 
        return False
      else:
        return self.left.contains(target)
  
    # else: target > self.value:
    else:
      if not self.right:
      # if self.right == None:
        return False
      return self.right.contains(target)

  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value

    # Can also do:
    # target = self
    # max_value = 0
    # while target:
    #   max_value = target.value
    #   target = target.right
    # return max_value

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)