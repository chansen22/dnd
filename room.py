from monster import *
from treasure import *
class Room():
  def __init__(self, data):
    self.treasureId = data.pop()
    self.monsterId = data.pop()
    self.roomDesc = data.pop()
    self.roomId = data.pop()

  def display(self):
    print("Id:",self.roomId, "Desc:",self.roomDesc, "Monster Id:",self.monsterId, "Treasure Id:",self.treasureId)

  def displayId(self):
    return self.roomId

  def name(self):
    return self.roomId
