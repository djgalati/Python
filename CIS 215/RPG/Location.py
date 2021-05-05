class Location:
  name = ''
  zonemap = {}

  def __init__(self):
    '''contructor to initiate the Location class (Joshua)'''
    self.name = "Intro"
    self.zonemap = {
        'Crash Site': {
            'DESCRIPTION' : ['where the plane crashed'],
            'SPOT' : ['C2'],
            'SOLVED' : ['False'],
            'DISPLAY' : ['True'],
            'ACCESSES': ['Beach']
        },
        'Beach' : {
            'DESCRIPTION' : ['a beach'],
            'SPOT' : ['D3'],
            'SOLVED' : ['False'],
            'DISPLAY' : ['True'],
            'ACCESSES': ['Fishing Area']
        },
        'Fishing Area' : {
            'DESCRIPTION' : ['a place to fish'],
            'SPOT' : ['C3'],
            'SOLVED' : ['False'],
            'DISPLAY' : ['True'],
            'ACCESSES': ['Abandoned Campsite']
        },
        'Abandoned Campsite' : {
            'DESCRIPTION' : ['an old campsite'],
            'SPOT' : ['B3'],
            'SOLVED' : ['False'],
            'DISPLAY' : ['True'],
            'ACCESSES': ['Empty Land']
        },
        'Empty Land': {
            'DESCRIPTION' : ['just some trees'],
            'SPOT' : ['C1'],
            'SOLVED' : ['False'],
            'DISPLAY' : ['True'],
            'ACCESSES': ['Bunker']
        },
        'Bunker' : {
            'DESCRIPTION' : ['an old military bunker underground'],
            'SPOT' : ['D2'],
            'SOLVED' : ['False'],
            'DISPLAY' : ['True'],
            'ACCESSES': ['Secret Island']
        },
        'Secret Island' : {
            'DESCRIPTION' : ['an offshore Island where mysteries lie'],
            'SPOT' : ['D4'],
            'SOLVED' : ['False'],
            'DISPLAY' : ['True'],
            'ACCESSES': ['Hidden Cave']
        },
        'Hidden Cave' : {
            'DESCRIPTION' : ['just a naturally formed cave in the island'],
            'SPOT' : ['A2'],
            'SOLVED' : ['False'],
            'DISPLAY' : ['True'],
            'ACCESSES': ['Graveyard']
        },
        'Graveyard' : {
            'DESCRIPTION' : ['2 gravestones lie in a field'],
            'SPOT' : ['B1'],
            'SOLVED' : ['False'],
            'DISPLAY' : ['True'],
            'ACCESSES': ['Biohazard Area']
        },
        'Biohazard Area' : {
            'DESCRIPTION' : ['a place where you cant stay for long'],
            'SPOT' : ['A4'],
            'SOLVED' : ['False'],
            'DISPLAY' : ['True']
        },
        'END' : {
            'DESCRIPTION' : ['End of Game'],
            'SOLVED' : ['False'],
            'SPOT' : ['A3'],
            'DISPLAY' : ['True']
        }
    }

  def setDisplay(self):
    '''Returns True on first location visit and false other times, so story line does not get repeated (Dom)'''
    try:
      for word in (self.zonemap[self.name]['DISPLAY']):
        action = word
      if action == 'True':
        temp = self.zonemap[self.name]
        temp.pop('DISPLAY')
        temp.update({'DISPLAY' : ['False']})
        self.zonemap.pop(self.name)
        self.zonemap.update({self.name : temp})
        return "['True']" 
      else:
        return "['False']"
    except KeyError:
      return "['True']"

  def unlockEND(self):
    temp = self.zonemap['END']
    temp.pop('SOLVED')
    temp.update({'SOLVED' : ['True']})
    self.zonemap.pop("END")
    self.zonemap.update({"END" : temp})


  def activeLoc(self):
    '''Returns the current location in use (Dom)'''
    return self.name

  def show(self):
    '''Shows the game map for reference (Joshua)'''
    if self.name != 'Intro':
      print("                   ___                        ")
      print(" /\__/\___________/   \_________________\     ")
      print("/  A1  |   A2    |   A3   |      A4      \    ")
      print("------------------------------------------\   ")
      print("|    B1    |    B2  |    B3      |    B4   |  ")
      print("___________________________________________/  ")
      print("|    C1    |     C2     |    C3   |           ")
      print("_________________________________/            ")
      print("|    D1    |     D2     | D3 ___/             ")
      print("\____/-\__/---------\_______/     |   D4   |  ")
      '''
      print("                   ___                        ")
      print(" /\__/\___________/   \_________________\     ")
      print("/    | Hidden Cave |    | Biohazard Area \    ")
      print("------------------------------------------\   ")
      print("| Graveyard |         | Abandoned Campsite |  ")
      print("___________________________________________/  ")
      print("| Empty Land | crash site | Fishing Area |    ")
      print("_________________________________________/    ")
      print("|    | Bunker |  Beach /                      ")
      print("\____/-\__/---------\_/  | Secret Island |    ")
      '''

  def move(self):
    '''Contains all logic to move the user linearly through the game while discovering but allows for "quick travel" once any location is discovered (Dom)'''
    while True:
      if self.name == 'Intro':
        self.name = "Crash Site"
        temp = self.zonemap[self.name]
        temp.pop('SOLVED')
        temp.update({'SOLVED' : ['True']})
        self.zonemap.pop(self.name)
        self.zonemap.update({self.name : temp})
        return self.name
      else:
        print ("choose from the following list of locations to go: ")
        for place in self.zonemap:
           if str(self.zonemap[place]['SOLVED']) == "['True']":
             for word in self.zonemap[place]['SPOT']:
              print(word + ': ' +place)
        choice = input("where would you like to move to? You can also choose to Explore: ")
        if choice.lower() == 'explore':
          try:
            if self.zonemap[self.name]['ACCESSES'] != None:
              print("You decide to go exploring and you stumple upon a new place")
              self.name = self.zonemap[self.name]['ACCESSES']
              for place in self.zonemap:
                for word in self.name:
                  if place == word:
                    temp = self.zonemap[place]
                    temp.pop('SOLVED')
                    temp.update({'SOLVED' : ['True']})
              for word in self.name:
                self.zonemap.pop(word)
                self.zonemap.update({word : temp})
          except KeyError:
            print("there is no where else to explore")
            break
          for word in self.name:
            self.name = word.title()
            return word
        else:
          for place in self.zonemap:
            if choice == place:
              if str(self.zonemap[place]['SOLVED']) == "['True']":
                self.name = choice
                return self.name
              else:
                print("This is not a discovered location")
        
