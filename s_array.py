class SArray:

  def __init__(self, *items):
    self.items = items

  def __mul__(self, other):
    res = []
    for s_item in self.items:
      for o_item in other.items:
        res.append(s_item + o_item)
    return SArray(*res)