from Location import *

class Player:
  inventory = []
  name = ''
  gameMap = ''

  def __init__(self):
    '''Initializes Player class (Dom)'''
    self.name = input("Please enter your desired name: ")
    self.name = self.name.capitalize()
    self.gameMap = Location()
    self.inventory = []

  def addItem(self, item):
    '''Adds item to user iventory when picked up (Dom)'''
    self.inventory.append(item)

  def removeItem(self, item):
    '''Removes item from user inventory when it's used (Dom)'''
    self.inventory.remove(item)

  def getInventory(self):
    '''Returns user inventory when requested(Dom)'''
    return self.inventory

  def setName(self, name):
    '''Sets users name (dom)'''
    self.name = name

  def getName(self):
    '''Return users name (Dom)'''
    return self.name

  def currLoc(self):
    '''Calls activeLoc() in location class (Dom) '''
    return self.gameMap.activeLoc()

  def getDisplay(self):
    '''Calls Location class setDisplay() (Dom)'''
    return self.gameMap.setDisplay()

  def move(self):
    '''Calls for game map to be shown and for location move logic (dom)'''
    #List map and show location options
    if any("Open Barrel" in lis for lis in self.inventory):
      self.gameMap.unlockEND()
    self.gameMap.show()
    return self.gameMap.move()
