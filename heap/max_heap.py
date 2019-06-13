class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
  # insert adds the input value into the heap; 
  # this method should ensure that the inserted value is in the correct spot in the heap
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
  # delete removes and returns the 'topmost' value from the heap; 
  # this method needs to ensure that the heap property is maintained after the topmost element has been removed.
    if len(self.storage) == 0:
      return
    elif len(self.storage) == 1:
      return self.storage.pop(0)
    elif len(self.storage) > 1:
      prev_max = self.storage[0]
      self.storage.pop(0)
      new_max = max(self.storage)
      max_index = self.storage.index(new_max)
      self._bubble_up(max_index)
      for i in range(len(self.storage)):
        self._sift_down(i)
      return prev_max

  def get_max(self):
  # get_max returns the maximum value in the heap in constant time.
    return self.storage[0]

  def get_size(self):
  # get_size returns the number of elements stored in the heap.
    return len(self.storage)

  def _bubble_up(self, index):
  # _bubble_up moves the element at the specified index "up" the heap 
  # by swapping it with its parent if the parent's value is less than the value at the specified index.
   
  # keep bubbling up until we've either reached the top of the heap
  # or we've reached a point where the parent is higher prio
    while index > 0:
    # on a single bubble up iteration
    # get the parent index 
      parent = (index - 1) // 2
    # compare the child against the value of the parent
    # if the child's value is higher prio than its parent's value
      if self.storage[index] > self.storage[parent]:
      # swap them
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
      # update the child's index to be the new index it is now at
        index = parent
    # otherwise, child is at a valid spot
      else:
      # stop bubbling up
        break

  def _sift_down(self, index):
    # _sift_down grabs the indices of this element's children and determines which child has a larger value. 
    # If the larger child's value is larger than the parent's value, the child element is swapped with the parent.
    left_child = 2  * index + 1
    right_child = 2 * index + 2

  # See if we have BOTH Left && Right Children
    if left_child in range(len(self.storage)) and right_child in range(len(self.storage)):
      if self.storage[index] < self.storage[left_child] or self.storage[index] < self.storage[right_child]:
        if self.storage[left_child] > self.storage[right_child]:
          self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
        else:
          self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
    
    elif left_child in range(len(self.storage)):
      if self.storage[index] < self.storage[left_child]:
        self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
    
    elif right_child in range(len(self.storage)): 
      if self.storage[index] < self.storage[right_child]:
        self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]