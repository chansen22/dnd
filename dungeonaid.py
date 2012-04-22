#!/home/cthansen/344/sandbox/bin/python
from dungeon import *
from room import *
from monster import *
from treasure import *
import cPickle as pickle
from Tkinter import *
import ttk

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
      print('\n')
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
      print("\n")
    else:
      print("Monster list is empty\n")
    if self.treasureList:
      print("List of treasures:")
      for x in self.treasureList:
        x.display()
      print("\n")
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
        print(x.display())
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
      print("Room Id:", x.roomId)
      print("Monster Id:", x.monsterId)
      print("Treasure Id:", x.treasureId)
      print("Room Description:", x.roomDesc)
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

roomdata = []
roomdata.append(1)
roomdata.append("A dark room")
roomdata.append(2)
roomdata.append(3)
room = Room(roomdata)

monsterdata = []
monsterdata.append(2)
monsterdata.append("orcs")
monsterdata.append(20)
monster = Monster(monsterdata)

treasuredata = []
treasuredata.append(3)
treasuredata.append("5 gold")
treasuredata.append(5)
treasure = Treasure(treasuredata)

dungeonAid.dungeon.addRoom(room, treasure, monster)

#while input is not None:
#  print("What would you like to do?")
#  print("0. Quits")
#  print("1. Create a new treasure")
#  print("2. Create a new monster")
#  print("3. Create a new room")
#  print("4. Delete a room")
#  print("5. Delete a treasure")
#  print("6. Delete a monster")
#  print("7. Display dungeon")
#  print("8. Save the dungeon")
#  print("9. Load a dungeon")
#  choice = input()
#
#  if choice == 0:
#    break
#  if choice == 1:
#    dungeonAid.createTreasure()
#  if choice == 2:
#    dungeonAid.createMonster()
#  if choice == 3:
#    dungeonAid.createRoom()
#  if choice == 4:
#    dungeonAid.deleteRoom()
#  if choice == 5:
#    dungeonAid.deleteTreasure()
#  if choice == 6:
#    dungeonAid.deleteMonster()
#  if choice == 7:
#    dungeonAid.displayDungeon()
#  if choice == 8:
#    dungeonAid.saveDungeon()
#  if choice == 9:
#    dungeonAid.loadDungeon()

root = Tk()
root.title("Dungeon Aid")

mainframe = Frame(root)
mainframe.pack()

fileframe = Frame(mainframe)
fileframe.pack(side = TOP)

spacingframe = Frame(fileframe)
spacingframe.pack(side = LEFT)
spacingframe["width"] = 250

quitframe = Frame(fileframe)
quitframe.pack(side = RIGHT)
quitbutton = Button(quitframe)
quitbutton["text"] = "Quit"
quitbutton["fg"] = "Red"
quitbutton["command"] = quitframe.quit
quitbutton.pack(side = RIGHT)

class Addroomtextframe:
  def __init__(self):
    top  =  self.top  =  Toplevel(mainframe)
    textframe = Frame(top)
    textframe.pack(side = TOP)
    titleframe = Frame(textframe)
    titleframe.pack(side = TOP)
    idframe = Frame(textframe)
    idframe.pack(side = TOP)
    descframe = Frame(textframe)
    descframe.pack(side = TOP)
    listframe = Frame(textframe)
    listframe.pack(side = TOP)
    buttonframe = Frame(textframe)
    buttonframe.pack(side = TOP)
    monsterframe = Frame(listframe)
    monsterframe.pack(side = LEFT)
    treasureframe = Frame(listframe)
    treasureframe.pack(side = RIGHT)
    addbuttonframe = Frame(buttonframe)
    addbuttonframe.pack(side = LEFT)
    cancelbuttonframe = Frame(buttonframe)
    cancelbuttonframe.pack(side = RIGHT)

    titlelabel = Label(titleframe)
    titlelabel["text"] = "Add Room"
    titlelabel.pack(side = TOP)

    idlabel = Label(idframe)
    idlabel["text"] = "Id:"
    idlabel.pack(side = LEFT, padx = 5)
    identry = Entry(idframe)
    identry.pack(side = RIGHT, padx = 5)

    desclabel = Label(descframe)
    desclabel["text"] = "Desc:"
    desclabel.pack(side = LEFT, padx = 5, pady = 5)
    descentry = Entry(descframe)
    descentry.pack(side = RIGHT, padx = 5, pady = 5)

    monsterlist = Listbox(monsterframe)
    monsterlist.pack(side = LEFT, pady = 5)
    monsterscrollbar = Scrollbar(monsterframe)
    monsterscrollbar.pack(side = LEFT)
    monsterlist.config(yscrollcommand = monsterscrollbar.set)
    monsterscrollbar.config(command = monsterlist.yview)

    treasurelist = Listbox(treasureframe)
    treasurelist.pack(side = LEFT, pady = 5)
    treasurescrollbar = Scrollbar(treasureframe)
    treasurescrollbar.pack(side = LEFT)
    treasurelist.config(yscrollcommand = treasurescrollbar.set)
    treasurescrollbar.config(command = treasurelist.yview)

    addbutton = Button(addbuttonframe)
    addbutton["text"] ="Add"
    #addbutton["command"] = ADD ROOM HERE
    addbutton.pack(side = LEFT)
    cancelbutton = Button(cancelbuttonframe)
    cancelbutton["text"] ="Cancel"
    cancelbutton["fg"] ="Red"
    cancelbutton["command"] = lambda: top.destroy()
    cancelbutton.pack(side = RIGHT)

    top.transient()

roomframe = Frame(mainframe)
roomframe.pack(side = TOP)

roombottomframe = Frame(mainframe)
roombottomframe.pack(side = BOTTOM)

roomlist = Listbox(roomframe)
roomlist.pack(side = LEFT)

scrollbar = Scrollbar(roomframe)
scrollbar.pack(side = LEFT, fill = Y)
roomlist.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = roomlist.yview)

listofrooms = dungeonAid.dungeon.rooms
for each in listofrooms:
  roomlist.insert(END, each.name)

roomentry = Entry(roomframe)
roomentry["width"] = 15
roomentry.pack(side = RIGHT)

roomaddbutton = Button(roombottomframe)
roomaddbutton["text"] = "Add"
roomaddbutton["command"] = lambda: Addroomtextframe()
roomaddbutton.pack(side = LEFT)

mainframe.mainloop()

