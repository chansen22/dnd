class Treasure:
  def __init__(self, data):
    self.treasureId = data[0]
    self.desc = data[1]
    self.value = data[2]

  def display(self):
    print("Id:", self.treasureId, "Desc:", self.desc, "Value:", self.value)

  def displayId(self):
    return self.treasureId
