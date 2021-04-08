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

  @children.setter
  def add_child(self, child):
   if child not in self._children:
     child._parent = self
     self._children.append(child)

  @children.setter
  def remove_child(self,child):
   child._parent = None
   self._children.remove(child)

  @parent.setter
  def parent(self, parent):
    # self._parent = parent
    if self._parent:
      self._parent.remove_child = self
    parent.add_child = self


node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

print(node1.children)
print(node2.children)
