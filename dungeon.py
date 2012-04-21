from room import *
from monster import *
from treasure import *
class Dungeon:

  def __init__(self):
    self.rooms = []
    self.monsters = []
    self.treasures = []

  def addRoom(self, room, treasure, monster):
    self.rooms.append(room)
    self.treasures.append(treasure)
    self.monsters.append(monster)

  def removeRoom(self, room):
    self.rooms.remove(room)
