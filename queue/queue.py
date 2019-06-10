class Node:
    def __init__(self, value=None, next_node=None):
        # its own value
        self.value = value
        # the next node in the list
        self.next_node = next_node

    def get_value(self):
        # return the value of this node
        return self.value

    def get_next(self):
        # return a reference to this node's next_node property
        return self.next_node

    def set_next(self, new_next):
        # set this node's `next_node` property
        self.next_node = new_next


class Queue:
    def __init__(self):
        self.size = 0
        # reference the first node in the linked list
        self.head = None
        # reference to the last node in the linked list
        self.tail = None

  
  # enqueue should add an item to the back of the queue (the tail).
    def enqueue(self, value):
        # wrap the value in a node 
        new_node = Node(value)
        # check if we're in an empty list state
        # we have an empty linked list
        # check the head reference
        if not self.head and not self.tail:
            # set the list's head reference to point to new_node
            self.head = new_node
            # set the list's tail reference to point to new_node 
            self.tail = new_node
        # every other case
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    # dequeue should remove and return an item from the front of the queue (the head).
    def dequeue(self):
        # make sure our list isn't empty
        if not self.head and not self.tail:
            return None
        # store a reference to the node we're removing 
        old_head_value = self.head.value
        # we only have a single node in the list
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return old_head_value
        # we have at least two nodes in the list
        else:
            # move the self.head reference to refer
            # to the old head's next node
            self.head = self.head.get_next()
            return old_head_value

    def len(self):
        length = 0
        current_value = self.head

        while current_value != None:
            length += 1
            current_value = current_value.get_next()
        self.size = length

        return self.size
