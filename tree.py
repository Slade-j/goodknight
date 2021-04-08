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





node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

print(node1.children)
print(node2.children)
