import sys,time,random,os
import pickle 
from player import *
import generator
'''Outline of engine was taken from https://github.com/dtaivpp/text_rpg_engine/blob/master/game_engine.py in order to give our team a starting point'''

def get_input(inputs: list, story, user):
  '''Takes user input and uses logic to take the proper action to move forward with game (Dom)'''
  while True:
    user_entered = input()
    user_entered = user_entered.title()
    isValid = False
    for item in inputs:
      if user_entered in item:
        isValid = True
    if isValid:
      if user_entered.lower() == 'move':
        return user.move()
        break
      else:
        temp = story.get(user.currLoc())
        temp = temp['Actions']
        temp = temp.pop(int(user_entered)-1)
        #Something weird is going on with where it grabs it from
        user.addItem(temp)
        print (user.getInventory())
        print("Anything else?")
    else:
      print("Invalid input. Please use one of the following inputs:\n")
      for things in inputs:
        print(things)
      user_entered = None


def display_page_text(lines):
  '''Take directly from Github, no modifications made, Prints locational text while traversing map'''
  typing_speed = 125 #wpm
  for line in lines:
    for word in line:
      sys.stdout.write(word)
      sys.stdout.flush()
      time.sleep(random.random()*10.0/typing_speed)
      
    time.sleep(1)
    # Make the user press enter to see the next line
    print('\n\nPress enter to continue')
    input()

def clear():
  '''Emptys screen when traversing to new location to keep clarity'''
  print('\n'*50)

def story_flow(story, user):
  '''Is a loop that contains the story flow by progressing through the binary file'''
  while user.currLoc() != "END":
    if user.currLoc() != None:
      loc = story.get(user.currLoc())
    clear()
    try:
      if (user.getDisplay()) == "['True']":
        display_page_text(loc['Text'])
    except TypeError:
      print ("That is not a valid location, please try again")
      user.move()
      while user.currLoc() == None:
        print ("That is not a valid location, please try again")
        print(loc)
        print(user.currLoc())
        user.move()
      break
    if user.currLoc() == "Intro":
        user.move()
    else:
      print(user.getName() + ', please choose an action from the following list:\n')
      for item in loc['Actions']:
        print (item)
      get_input(loc['Actions'], story, user)
  loc = story.get('END')
  display_page_text(loc['Text'])

def main():
  #Start of Program
  story = {}
  user = Player()
  print("Hello " + user.getName() +", Press enter to begin")
  input()
  clear()
  with open('Test.ch', 'rb') as active:
    story = pickle.load(active)
    story_flow(story, user)

if __name__ == "__main__":
  exit(main())
