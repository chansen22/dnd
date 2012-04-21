class Monster:
  def __init__(self, data):
    self.monsterHits = data.pop()
    self.monsterType = data.pop()
    self.monsterId = data.pop()

  def display(self):
    print "Type:", self.monsterType, "Id:", self.monsterId, "Hits:", self.monsterHits

  def displayId(self):
    return self.monsterId
