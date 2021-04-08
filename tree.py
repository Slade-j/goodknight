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
      child.add_parent = self._value
      self._children.append(child)
