class Treasure:
  def __init__(self, data):
    self.value = data.pop()
    self.desc = data.pop()
    self.treasureId = data.pop()

  def display(self):
    print "Id:", self.treasureId, "Desc:", self.desc, "Value:", self.value

  def displayId(self):
    return self.treasureId
