#!/home/cthansen/344/sandbox/bin/python
from dungeon import *
from room import *
from monster import *
from treasure import *
import cPickle as pickle
from Tkinter import *
import ttk

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

roomaddbutton = Button(roombottomframe)
roomaddbutton["text"] = "Add"
roomaddbutton["command"] = lambda: Addroomtextframe()
roomaddbutton.pack(side = LEFT)

roomInfoFrame = Frame(roomframe)
roomInfoFrame.pack(side = RIGHT)

roomInfoListFrame = Frame(roomInfoFrame)
roomInfoListFrame.pack(side = BOTTOM)

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

monsterInfoFrame = Frame(monsterFrame)
monsterInfoFrame.pack(side = RIGHT)

#TREASURE FRAME
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

treasureInfoFrame = Frame(treasureFrame)
treasureInfoFrame.pack(side = RIGHT)

class DungeonAid:
  def __init__(self):
    self.dungeon = Dungeon()
    self.roomList = []
    self.treasureList = []
    self.monsterList = []
    self.monsterListBox = Listbox(monsterFrame)
    self.monsterListBox.pack(side = LEFT)
    self.monsterListBox.bind("<Double-Button-1>", self.getMonsterInfo)
    self.treasureListBox = Listbox(treasureFrame)
    self.treasureListBox.pack(side = LEFT)
    self.treasureListBox.bind("<Double-Button-1>", self.getTreasureInfo)
    self.roomListBox = Listbox(roomframe)
    self.roomListBox.pack(side = LEFT)
    self.roomListBox.bind("<Double-Button-1>", self.getRoomInfo)
    self.roomInfoListBox = Listbox(roomInfoListFrame)
    self.roomInfoListBox.pack(side = LEFT)

    self.monsterInfoId = Label(monsterInfoFrame)
    self.monsterInfoId["text"] = "Monster Id: "
    self.monsterInfoId.pack()

    self.monsterInfoDesc = Label(monsterInfoFrame)
    self.monsterInfoDesc["text"] = "Monster Desc: "
    self.monsterInfoDesc.pack()

    self.monsterInfoHits= Label(monsterInfoFrame)
    self.monsterInfoHits["text"] = "Monster Hits: "
    self.monsterInfoHits.pack()

    self.treasureInfoId = Label(treasureInfoFrame)
    self.treasureInfoId["text"] = "Treasure Id: "
    self.treasureInfoId.pack()

    self.treasureInfoDesc = Label(treasureInfoFrame)
    self.treasureInfoDesc["text"] = "Treasure Desc: "
    self.treasureInfoDesc.pack()

    self.treasureInfoHits= Label(treasureInfoFrame)
    self.treasureInfoHits["text"] = "Treasure Value: "
    self.treasureInfoHits.pack()

    self.roomInfoId = Label(roomInfoFrame)
    self.roomInfoId["text"] = "Room Id: "
    self.roomInfoId.pack()

    self.roomInfoDesc = Label(roomInfoFrame)
    self.roomInfoDesc["text"] = "Room Desc: "
    self.roomInfoDesc.pack()

  def updateMonsterList(self):
    self.monsterListBox.delete(0, END)
    for each in self.monsterList:
      self.monsterListBox.insert(END, each.monsterId)

  def updateTreasureList(self):
    self.treasureListBox.delete(0, END)
    for each in self.treasureList:
      self.treasureListBox.insert(END, each.treasureId)

  def updateRoomList(self):
    self.roomListBox.delete(0, END)
    for each in self.dungeon.rooms:
      self.roomListBox.insert(END, each.roomId)
  
  def getMonsterInfo(self, event):
    item = self.monsterListBox.curselection()
    stuff = int(item[0])
    self.monsterInfoId["text"] = "Monster Id: " + self.monsterList[stuff].monsterId
    self.monsterInfoDesc["text"] = "Monster Type: " + self.monsterList[stuff].monsterType
    self.monsterInfoHits["text"] = "Monster Hits: " + self.monsterList[stuff].monsterHits

  def getTreasureInfo(self, event):
    item = self.treasureListBox.curselection()
    stuff = int(item[0])
    self.treasureInfoId["text"] = "Treasure Id: " + self.treasureList[stuff].treasureId
    self.treasureInfoDesc["text"] = "Treasure Type: " + self.treasureList[stuff].desc
    self.treasureInfoHits["text"] = "Treasure Value: " + self.treasureList[stuff].value

  def getRoomInfo(self, event):
    item = self.roomInfoListBox.curselection()
    stuff = int(item[0])
    self.roomInfoId["text"] = "Room Id: " + self.roomList[stuff].roomId
    self.roomInfoDesc["text"] = "Room Desc: " + self.roomList[stuff].roomDesc
    self.roomInfoListBox.delete(0, END)
    #for each in self.roo

dungeonAid = DungeonAid()

scrollbar = Scrollbar(roomframe)
scrollbar.pack(side = LEFT, fill = Y)
dungeonAid.roomListBox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = dungeonAid.roomListBox.yview)

roomInfoScrollbar = Scrollbar(roomInfoListFrame)
roomInfoScrollbar.pack(side = LEFT, fill = Y)
dungeonAid.roomInfoListBox.config(yscrollcommand = roomInfoScrollbar.set)
roomInfoScrollbar.config(command = dungeonAid.roomInfoListBox.yview)

monsterButtonFrame = Frame(monsterMainFrame)
monsterButtonFrame.pack(side = BOTTOM)

monsterScrollbar = Scrollbar(monsterFrame)
monsterScrollbar.pack(side = LEFT, fill = Y)
dungeonAid.monsterListBox.config(yscrollcommand = monsterScrollbar.set)
monsterScrollbar.config(command = dungeonAid.monsterListBox.yview)

monsterAddButton = Button(monsterButtonFrame)
monsterAddButton["text"] = "Add"
monsterAddButton["command"] = lambda: AddMonsterTextFrame()
monsterAddButton.pack(side = LEFT)

treasureButtonFrame = Frame(treasureMainFrame)
treasureButtonFrame.pack(side = BOTTOM)

treasureScrollbar = Scrollbar(treasureFrame)
treasureScrollbar.pack(side = LEFT, fill = Y)
dungeonAid.treasureListBox.config(yscrollcommand = treasureScrollbar.set)
treasureScrollbar.config(command = dungeonAid.treasureListBox.yview)

treasureAddButton = Button(treasureButtonFrame)
treasureAddButton["text"] = "Add"
treasureAddButton["command"] = lambda: AddTreasureTextFrame()
treasureAddButton.pack(side = LEFT)

class AddTreasureTextFrame:
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
    valueframe = Frame(textframe)
    valueframe.pack(side = TOP)
    listframe = Frame(textframe)
    listframe.pack(side = TOP)
    buttonframe = Frame(textframe)
    buttonframe.pack(side = TOP)
    addbuttonframe = Frame(buttonframe)
    addbuttonframe.pack(side = LEFT)
    cancelbuttonframe = Frame(buttonframe)
    cancelbuttonframe.pack(side = RIGHT)

    titlelabel = Label(titleframe)
    titlelabel["text"] = "Add Treasure"
    titlelabel.pack(side = TOP)

    idlabel = Label(idframe)
    idlabel["text"] = "Id:"
    idlabel.pack(side = LEFT, padx = 5)
    self.identry = Entry(idframe)
    self.identry.pack()

    desclabel = Label(descframe)
    desclabel["text"] = "Desc:"
    desclabel.pack(side = LEFT, padx = 5, pady = 5)
    self.descentry = Entry(descframe)
    self.descentry.pack()

    valueLabel = Label(valueframe)
    valueLabel["text"] = "Value:"
    valueLabel.pack(side = LEFT)
    self.valueEntry = Entry(valueframe)
    self.valueEntry.pack()

    addbutton = Button(addbuttonframe)
    addbutton["text"] ="Add"
    addbutton["command"] = lambda: self.createTreasure()
    addbutton.pack(side = LEFT)
    cancelbutton = Button(cancelbuttonframe)
    cancelbutton["text"] ="Cancel"
    cancelbutton["fg"] ="Red"
    cancelbutton["command"] = lambda: self.top.destroy()
    cancelbutton.pack(side = RIGHT)

    self.top.transient()

  def createTreasure(self):
    treasureData = []
    treasureData = (self.identry.get(), self.descentry.get(), self.valueEntry.get())
    treasure = Treasure(treasureData)
    dungeonAid.treasureList.append(treasure)
    dungeonAid.updateTreasureList()
    self.top.destroy()

class AddMonsterTextFrame:
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
    hitsframe = Frame(textframe)
    hitsframe.pack(side = TOP)
    listframe = Frame(textframe)
    listframe.pack(side = TOP)
    buttonframe = Frame(textframe)
    buttonframe.pack(side = TOP)
    addbuttonframe = Frame(buttonframe)
    addbuttonframe.pack(side = LEFT)
    cancelbuttonframe = Frame(buttonframe)
    cancelbuttonframe.pack(side = RIGHT)

    titlelabel = Label(titleframe)
    titlelabel["text"] = "Add Monster"
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

    hitsLabel = Label(hitsframe)
    hitsLabel["text"] = "Hits:"
    hitsLabel.pack(side = LEFT, padx = 5, pady = 5)
    self.hitsentry = Entry(hitsframe)
    self.hitsentry.pack(side = RIGHT, padx = 5, pady = 5)

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
    monsterData = []
    monsterData = (self.identry.get(), self.descentry.get(), self.hitsentry.get())
    monster = Monster(monsterData)
    dungeonAid.monsterList.append(monster)
    dungeonAid.updateMonsterList()
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

root.mainloop()
