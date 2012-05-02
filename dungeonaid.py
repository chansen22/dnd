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

dungeonAid = DungeonAid()

roomdata = []
roomdata.append("Room 1")
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

root = Tk()
root.title("Dungeon Aid")

n = ttk.Notebook(root)
n.pack(side = TOP)
roomTab = ttk.Frame(n)
monsterTab = ttk.Frame(n)
treasureTab = ttk.Frame(n)
n.add(roomTab, text="Room")
n.add(monsterTab, text="Monster")
n.add(treasureTab, text="Treasure")

class AddMonsterTextFrame:
  def __init(self):
    self.top  =  self.top  =  Toplevel(mainframe)
    textframe = Frame(self.top)
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
    self.identry = Entry(idframe)
    self.identry.pack(side = RIGHT, padx = 5)

    desclabel = Label(descframe)
    desclabel["text"] = "Desc:"
    desclabel.pack(side = LEFT, padx = 5, pady = 5)
    self.descentry = Entry(descframe)
    self.descentry.pack(side = RIGHT, padx = 5, pady = 5)

    addbutton = Button(addbuttonframe)
    addbutton["text"] ="Add"
    addbutton["command"] = lambda: self.createMonster()
    addbutton.pack(side = LEFT)
    cancelbutton = Button(cancelbuttonframe)
    cancelbutton["text"] ="Cancel"
    cancelbutton["fg"] ="Red"
    cancelbutton["command"] = lambda: self.top.destroy()
    cancelbutton.pack(side = RIGHT)

    self.top.transient()

  def createMonster(self):
    monsterList = []
    self.top.destroy()

class Addroomtextframe:
  def __init__(self):
    self.top  =  self.top  =  Toplevel(mainframe)
    textframe = Frame(self.top)
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
    self.identry = Entry(idframe)
    self.identry.pack(side = RIGHT, padx = 5)

    desclabel = Label(descframe)
    desclabel["text"] = "Desc:"
    desclabel.pack(side = LEFT, padx = 5, pady = 5)
    self.descentry = Entry(descframe)
    self.descentry.pack(side = RIGHT, padx = 5, pady = 5)

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
    addbutton["command"] = lambda: self.createRoom()
    addbutton.pack(side = LEFT)
    cancelbutton = Button(cancelbuttonframe)
    cancelbutton["text"] ="Cancel"
    cancelbutton["fg"] ="Red"
    cancelbutton["command"] = lambda: self.top.destroy()
    cancelbutton.pack(side = RIGHT)

    self.top.transient()

  def createRoom(self):
    stackOfInfo = []
    stackOfInfo = (self.identry.get(), self.descentry.get())
    print "Room id entered is: ", stackOfInfo[0], " and desc entered is: ", stackOfInfo[1] 
    self.top.destroy()

#MAIN ROOM FRAME
mainframe = Frame(roomTab)
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
  roomlist.insert(END, each.roomId)

roomentry = Entry(roomframe)
roomentry["width"] = 15
roomentry.pack(side = RIGHT)

roomaddbutton = Button(roombottomframe)
roomaddbutton["text"] = "Add"
roomaddbutton["command"] = lambda: Addroomtextframe()
roomaddbutton.pack(side = LEFT)

#MONSTER FRAME
monsterMainFrame = Frame(monsterTab)
monsterMainFrame.pack()
monsterFileFrame = Frame(monsterMainFrame)
monsterFileFrame.pack()
monsterSpacingFrame = Frame(monsterFileFrame)
monsterSpacingFrame.pack(side = LEFT)
monsterSpacingFrame["width"] = 250

monsterQuitFrame = Frame(monsterFileFrame)
monsterQuitFrame.pack(side = RIGHT)
monsterQuitButton = Button(monsterQuitFrame)
monsterQuitButton["text"] = "Quit"
monsterQuitButton["fg"] = "Red"
monsterQuitButton["command"] = monsterQuitFrame.quit
monsterQuitButton.pack(side = RIGHT)

monsterFrame = Frame(monsterMainFrame)
monsterFrame.pack(side = TOP)

monsterButtonFrame = Frame(monsterMainFrame)
monsterButtonFrame.pack(side = BOTTOM)

monsterList = Listbox(monsterFrame)
monsterList.pack(side = LEFT)

monsterScrollbar = Scrollbar(monsterFrame)
monsterScrollbar.pack(side = LEFT, fill = Y)
monsterList.config(yscrollcommand = monsterScrollbar.set)
monsterScrollbar.config(command = monsterList.yview)

listOfMonsters = dungeonAid.dungeon.monsters
for each in listOfMonsters:
  monsterList.insert(END, each.monsterId)

monsterAddButton = Button(monsterButtonFrame)
monsterAddButton["text"] = "Add"
monsterAddButton["command"] = lambda: AddMonsterTextFrame()
monsterAddButton.pack(side = LEFT)

#MONSTER FRAME
treasureMainFrame = Frame(treasureTab)
treasureMainFrame.pack()
treasureFileFrame = Frame(treasureMainFrame)
treasureFileFrame.pack()
treasureSpacingFrame = Frame(treasureFileFrame)
treasureSpacingFrame.pack(side = LEFT)
treasureSpacingFrame["width"] = 250

treasureQuitFrame = Frame(treasureFileFrame)
treasureQuitFrame.pack(side = RIGHT)
treasureQuitButton = Button(treasureQuitFrame)
treasureQuitButton["text"] = "Quit"
treasureQuitButton["fg"] = "Red"
treasureQuitButton["command"] = treasureQuitFrame.quit
treasureQuitButton.pack(side = RIGHT)

treasureFrame = Frame(treasureMainFrame)
treasureFrame.pack(side = TOP)

treasureButtonFrame = Frame(treasureMainFrame)
treasureButtonFrame.pack(side = BOTTOM)

treasureList = Listbox(treasureFrame)
treasureList.pack(side = LEFT)

treasureScrollbar = Scrollbar(treasureFrame)
treasureScrollbar.pack(side = LEFT, fill = Y)
treasureList.config(yscrollcommand = treasureScrollbar.set)
treasureScrollbar.config(command = treasureList.yview)

listOfTreasures = dungeonAid.dungeon.treasures
for each in listOfTreasures:
  treasureList.insert(END, each.treasureId)

treasureAddButton = Button(treasureButtonFrame)
treasureAddButton["text"] = "Add"
treasureAddButton["command"] = lambda: AddTreasureTextFrame()
treasureAddButton.pack(side = LEFT)

root.mainloop()
