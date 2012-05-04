class Monster:
  def __init__(self, data):
    self.monsterId = data[0]
    self.monsterType = data[1]
    self.monsterHits = data[2]

  def display(self):
    print("Type:", self.monsterType, "Id:", self.monsterId, "Hits:", self.monsterHits)

  def displayId(self):
    return self.monsterId
