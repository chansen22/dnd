#!/usr/bin/python2
from dungeon import *
from room import *
from monster import *
from treasure import *
import cPickle as pickle

class DungeonAid:
  def __init__(self):
    self.dungeon = Dungeon()
    self.treasureList = []
    self.monsterList = []

  def createTreasure(self):
    print("Please enter a treasure Id, description and value")
    print("Ex: 3 \n\"20 Shiny pieces of gold!\" \n20\n0 quits")
    if self.treasureList:
      print("List of treasures:")
      for x in self.treasureList:
        x.display()
    else:
      print("Treasure list is empty\n")
    treasureData = []
    while input is not None:
      id = int(input())
      if id == 0:
        break
      treasureData.append(id)
      desc = input()
      treasureData.append(desc)
      value = input()
      treasureData.append(value)
      break
    if id != 0:
      treasure = Treasure(treasureData)
      self.treasureList.append(treasure)

  def createMonster(self):
    print("Please enter a monster Id, a type and number of hits")
    print("Ex: 5 \n\"5 orcs\" \n20\n0 quits")
    if self.monsterList:
      print("List of monsters:")
      for x in self.monsterList:
        x.display()
      print "\n"
    else:
      print("Monster list is empty\n")
    monsterData = []
    while input is not None:
      id = int(input())
      if id == 0:
        break
      monsterData.append(id)
      desc = input()
      monsterData.append(desc)
      hits = int(input())
      monsterData.append(hits)
      break
    if id != 0:
      monster = Monster(monsterData)
      self.monsterList.append(monster)

  def createRoom(self):
    print("Please enter a room Id, description, monster Id and treasure Id")
    print("Ex: 5 \n\"A dark and smelly room\" \n3 \n4\n0 quits")
    if self.monsterList:
      print("List of monsters:")
      for x in self.monsterList:
        x.display()
      print "\n"
    else:
      print("Monster list is empty\n")
    if self.treasureList:
      print("List of treasures:")
      for x in self.treasureList:
        x.display()
      print "\n"
    else:
      print("Treasure list is empty\n")
    roomData = []
    while input is not None:
      id = input()
      if id == 0:
        break
      roomData.append(id)
      desc = input()
      roomData.append(desc)
      monsterId = input()
      roomData.append(monsterId)
      treasureId = input()
      roomData.append(treasureId)
      break
    if id != 0:
      room = Room(roomData)
      for x in self.treasureList:
        if treasureId == x.displayId():
          treasure = x
      for x in self.monsterList:
        if monsterId == x.displayId():
          monster = x
      self.dungeon.addRoom(room, treasure, monster)

  def deleteRoom(self):
    print("Please enter a room Id")
    print("Ex: 5")
    print("0 to quit")
    if self.dungeon.rooms:
      print("List of rooms")
      for x in self.dungeon.rooms:
        print x.display()
    else:
      print("Room list is empty\n")
    roomId = (int(input()))
    if roomId == 0:
      roomId = 1
    else:
      for x in self.dungeon.rooms:
        if (int(roomId)) == x.displayId():
          self.dungeon.rooms.remove(x)

  def deleteTreasure(self):
    print("Please enter a treasure Id to delete")
    print("Ex: 5")
    print("0 to quit")
    if self.treasureList:
      print("List of treasures:")
      for x in self.treasureList:
        x.display()
        print("\n")
    else:
      print("Treasure list is empty\n")
    treasureData = []
    treasureData = input()
    if treasureData != 0:
      isInDungeon = 0
      if self.dungeon.treasures:
        for x in self.dungeon.treasures:
          if x.displayId() == treasureData:
            isInDungeon = 1
            print("Treasure is in the dungeon, so it will not be removed")
      if isInDungeon == 0:
        if self.treasureList:
          for x in self.treasureList:
            if x.displayId() == treasureData:
              self.treasureList.remove(x)

  def deleteMonster(self):
    print("Please enter a monster Id to delete")
    print("Ex: 5")
    print("0 to quit")
    if self.monsterList:
      print("List of monsters:")
      for x in self.monsterList:
        x.display()
        print("\n")
    else:
      print("Monster list is empty\n")
    monsterData = []
    monsterData = input()
    if monsterData!= 0:
      isInDungeon = 0
      if self.dungeon.monsters:
        for x in self.dungeon.monsters:
          if x.displayId() == monsterData:
            isInDungeon = 1
            print("Monster is in the dungeon, so it will not be removed")
      if isInDungeon == 0:
        if self.monsterList:
          for x in self.monsterList:
            if x.displayId() == monsterData:
              self.monsterList.remove(x)

  def displayDungeon(self):
    print("Dungeon:")
    print("Rooms:")
    for x in self.dungeon.rooms:
      print "Room Id:", x.roomId
      print "Monster Id:", x.monsterId
      print "Treasure Id:", x.treasureId
      print "Room Description:", x.roomDesc
      print("\n")

  def saveDungeon(self):
    print("Please enter the name you would like to save your dungeon as")
    print("Ex: \"myfirstdungeon\"")
    print("0 to quit")
    name = input()
    if name == 0:
      name = 1
    else:
      output = open(name, 'wb')
      pickle.dump(self.dungeon, output)
      output.close()

  def loadDungeon(self):
    print("Please enter the name of the dungeon you would like to load")
    print("Ex: \"myfirstdungeon\"")
    print("0 to quit")
    name = input()
    if name == 0:
      name = 1
    else:
      dungeonIn = open(name, 'r')
      inFile = pickle.load(dungeonIn)
      dungeonIn.close()
      self.dungeon = inFile
      self.treasureList = []
      self.monsterList = []
      for x in self.dungeon.treasures:
        self.treasureList.append(x)
      for x in self.dungeon.monsters:
        self.monsterList.append(x)

dungeonAid = DungeonAid()

while input is not None:
  print("What would you like to do?")
  print("0. Quits")
  print("1. Create a new treasure")
  print("2. Create a new monster")
  print("3. Create a new room")
  print("4. Delete a room")
  print("5. Delete a treasure")
  print("6. Delete a monster")
  print("7. Display dungeon")
  print("8. Save the dungeon")
  print("9. Load a dungeon")
  choice = input()

  if choice == 0:
    break
  if choice == 1:
    dungeonAid.createTreasure()
  if choice == 2:
    dungeonAid.createMonster()
  if choice == 3:
    dungeonAid.createRoom()
  if choice == 4:
    dungeonAid.deleteRoom()
  if choice == 5:
    dungeonAid.deleteTreasure()
  if choice == 6:
    dungeonAid.deleteMonster()
  if choice == 7:
    dungeonAid.displayDungeon()
  if choice == 8:
    dungeonAid.saveDungeon()
  if choice == 9:
    dungeonAid.loadDungeon()
