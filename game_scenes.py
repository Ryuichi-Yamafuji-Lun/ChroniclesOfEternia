from sys import exit
from textwrap import dedent

class Scene(object):
  
  def enter(self):
    print("Scene not configured")
    exit(1)

class Death(Scene):
  
  def enter(self):
    print("You Die")
    exit(1)

class StartingScreen(Scene):
  
  def enter(self):
    print("Welcome")
    action = input(" 1 or 2: ")
    if action == "1":
      return 'death'

    else:
      return 'begin'

class Beginning(Scene):

    def enter(self):
      print("Begin")
      return 'forest'  

class Forest(Scene):

    def enter(self):
      print("Forest")
      return 'plain'  

class Plains(Scene):

    def enter(self):
      print("Plain")
      return 'mountain'
      
class Mountain(Scene):

    def enter(self):
      print("mountain")
      return 'm_ruin'

class MountainRuins(Scene):

    def enter(self):
      print("Ruin1")
      return 'kingdom'

class Kingdom(Scene):

    def enter(self):
      print("kingdom")
      return 'f_dungeon'
    
class FinalDungeon(Scene):

    def enter(self):
      print("Final Dungeon")
      return 'f_room'
    
class FinalRoom(Scene):

    def enter(self):
      print("Final Room")
      return 'finish'

class Finish(Scene):

    def enter(self):
      print("finish")