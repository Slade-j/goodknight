class Node:
  # __slots__ = ["_value", "_parent", "_children"]

  def __init__(self, value):
    self._value = value
    self._parent = None
    self._children = []

  @property
  def value(self):
    return self._value

  @property
  def children(self):
    return self._children

  @property
  def parent(self):
    return self._parent


  def add_child(self, child):
   if child not in self._children:
    #  if child._parent == self:
      self._children.append(child)
    #  else:
      child.parent = self


  def remove_child(self,child):
    if child in self._children:
      self._children.remove(child)
      child.parent = None

  @parent.setter
  def parent(self, parent):
    if self._parent is parent:
      return
    if self._parent:
      self._parent.remove_child(self)
    self._parent = parent
    if parent is not None:
      parent.add_child(self)

  def breadth_search(self, value):
    queue = [self]
    while queue:
      node = queue.pop(0)
      if node._value == value:
        return node
      else:
        for child in node._children:
          queue.append(child)

        # can extend without loop

  def depth_search(self, value):
    if self._value == value:
      return self
    for child in self._children:
      node = child.depth_search(value)
      if node is not None:
        return node


    # def depth_search(self, value):
    #   if self._value == value:
    #     return self
    #   for child in self._children:
    #     if child is not None:
    #       return child.depth_search(value)

  
  
  # def depth_search(self, value):
  #   if self._value == value:
  #     return self
  #   for child in self._children:
  #     return child.depth_search(value)
    







# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")
# node4 = Node("root4")
# node5 = Node("root5")
# node6 = Node("root6")

# node3.parent = node1
# node2.parent = node1
# node4.parent = node1
# node5.parent = node1
# node6.parent = node1

# print(node1.depth_search('bogus'))
