from sys import exit
from textwrap import dedent

#Fragment Total
fragment = 0

class Scene(object):
  
  def enter(self):
    print("Scene not configured")
    exit(1)

class Death(Scene):
  
  def enter(self):
    print("\t\t\t\t             You Died")
    exit(1)

class StartingScreen(Scene):
  
  def enter(self):
    print("\t\t\t\t---Chronicles of Eternia---")
    print("\t\t\t    Welcome to the Chronicles of Eternia")
    print("Press enter to start the game or press 1 to exit:")
    action = input("< ")
    if action == "1":
      exit(1)
    else:
      return 'begin'

class Beginning(Scene):

    def enter(self):
      print("-" * 90)
      print(dedent("""
      The Fallen have invaded your homeland killing off all of those with royal elvish blood.
      In an effort to save you the successor of the House of Yggdrasil, your father the King 
      takes a poisonous arrow and succumbing to the poison. In his last dying breath he hands 
      you a family heirloom an ancient artifact known as the 'Eternia Crystal' and the map to 
      all of the fragments. The Crystal is believed to be the key to unlocking an ancient
      weapon with immense power. In order to keep the weapon out of the Fallens hands and
      eradicate them you decide to travel across the realms to collect the fragments. You head
      to the first location of the fragment the Golden Plain.
      """))
      print("-" * 90)
      return 'plain'  

class Plains(Scene):

    def enter(self):
      print("\t\t\t\t      ---Golden Plain---")
      print("-" * 90)
      print(dedent("""
      As you make you way across the Golden Plain, you get surrounded by the Fallen with their
      corrupt arrows drawns.

      Press 1: Dodge
      Press 2: Fight
      Press 3: Flee
      """))
      
      while(True):
         action = input("< ")
         print("-" * 90)
         if action == "1":
            print("You try to dodge a barrage of bullets but you get hit.")
            print("With limited mobility the all of the second barage hits you")
            return 'death'
         elif action == "2":
            print(dedent(""" 
            You draw your arrow and let it fly. It hits one of the Fallen and the Fallen hesitate to shoot.
            Using this oppurtunity you run towards Dragonkeep Mountain.
            """))
            return 'mountain'
         elif action == '3':
            print(dedent("""
            You try to flee from the Fallen but get struck in the back and leg. As you try to flee back to the 
            Elven Forest the Fallen follow your trail of blood and capture you. You are then beheaded with the 
            other elves with royal descent.
            """))
            return 'death'
         else:
            print("\t\t\t\t     Please select actions")

      
class Mountain(Scene):

    def enter(self):
      print("\t\t\t\t   ---Dragonkeep Mountain---")
      print("-" * 90)
      print(dedent("""
      You escape into Dragonkeep Mountain with the Fallen on hot pursuit. You continue and the path splits into two.
       
      Press 1: Left Path
      Press 2: Right Path
      """))

      while True:
         action = input("< ")
         print("-" * 90)
         if action == "1":
            print("You run to the left path and you come across a broken bridge")
            print("With the Fallen still on hot pursuit you decide to jump")
            return "death"
         elif action == "2":
            print(dedent("""
            You run to the right path and come across a tiny cave hidden behind the boarder. You dive into the small cave and 
            see the Fallen run past you. The Eternal Cryatal start to react and point towards deeper into the cave so you continue.
            Once you reach the deepest part of the cave you come across a large stone door with languauges which you have never seen
            engraved into it.
            """))
            break
         else:
            print("Select options availbale")
         
      print("-" * 90)
      print(dedent("""
      The large store door seems to be operated by a mechnism with three stone tablet. Each of these stone tablets have a drawing 
      associated with them. the door has a slot about the width of the stone tablets. You think it might have something to do with 
      the mounatain. 

      Tablet 1: ≽゜﴿﴿﴿﴿彡

      Tablet 2: ᄽ❮ȍ∷ő❯ᄿ

      Tablet 3:  ,-
                ,-'    
                `=e
      """))   

      while True:
         action = input("< ")
         print("-" * 90)
         if action == "1":
            print(dedent("""
            You slide the first tablet into the slot and the stone door slowly opens. The smell of the sea can be smelled 
            which is very strange. The cave then rumbles and the path that you took gets closed off and the sound of water 
            can be heard from the stone door. Water then gushes in filling the cave. 
            """))
            return 'death'
         elif action == "2":
            print(dedent(""" 
            You slide the second tablet into the slot and the stone door opens quickly. A strong wind suddenly gushes behind
            you pulling you in and the stone door closes. You look around the dark room wondering what was going on. Then suddenly 
            you start to get dizzy and fall to the floor. You then lose concious.
            """))
            return 'death'
         elif action == '3':
            print(dedent("""
            You slide the third table into the slot and the stone door rumbles open. You then cautiously go in as the room lights up.
            The old ruin looks like a fort of some sort so you decide to proceed.
            """))
            return 'm_ruin'
         else:
            print("\t\t\t\t     Please select a tablet")
     

class MountainRuins(Scene):

    def enter(self):
      print("\t\t\t\t     ---Dragonkeep Ruin---")
      global fragment
      print("-" * 90)
      print(dedent("""
      As you go down a long hallway you see remnants all over the area. At the very end of the hallway there seems to be a table.
      You approach the table and see that there is a slot similar to the Eternal Crystal. You place the Eternal Crystal into the 
      table and the table splits open revealing an underground path. You take the Eternal Crystal and proceed. As you proceed down
      the path you see engraving of a dragon fighting the elves and the human. You inspect the dragon and see that its eyes can be 
      removed.

      Press 1: Remove
      Press 2: Not Remove
      """))
      while True:
         action = input("< ")
         print("-" * 90)
         if action == "1":
            print(dedent("""
            You remove the eye of the dragon and the eye crumbles revealing a fragment of the Eternal Crystal. The Fragment and
            the Eternal Cryatal shines brightly and conbine together. You continue down the path.
            """))
            fragment += 1
            break
         elif action == "2":
            print(dedent("""
            You proceed down the path. 
            """))
            break
         else:
            print("Please input correct options")
      print("-" * 90)
      print(dedent("""
      You get to the end of the path and enter a room. In the room there is a crystal shining brightly lighting up the room. 
      Would you like to take the crystal?

      Press 1: Take the cystal
      press 2: Don't take the crystal
      """))
      
      while True:
         action = input("< ")
         print("-" * 90)
         if action == "1":
            print("The crystal breaks apart in your hand and the room goes black")
            return 'death'
         elif action == "2":
            print("You decide to look around the room before you touch the crystal")
            break
         else:
            print("Please select proper action")
      print(dedent("""
      You look around the room and find a lever. You decide to pull the lever and a unstable portal appears.
      Would you like to proceed?

      Press 1: Proceed
      Press 2: Dont Proceed 
      """))

      while True:
         action = input("< ")
         print("-" * 90)
         if action == "1":
            print("You take the portal and it transport you somewhere")
            return 'kingdom'
         elif action == "2":
            print("The unstable portal closes and the crytal dissapears leaving you in the dark")
            return 'death'
         else:
            print("Select an action")

class Kingdom(Scene):

    def enter(self):
      print("\t\t\t\t       ---The Kingdom---")
      return 'f_dungeon'
    
class FinalDungeon(Scene):

    def enter(self):
      print("\t\t\t\t     ---Zephyrs Dungeon---")
      return 'f_room'
    
class FinalRoom(Scene):

    def enter(self):
      print("\t\t\t\t     ---The Throne Room---")
      return 'forest'

class Forest(Scene):

    def enter(self):
      print("\t\t\t\t       ---Elven Forest---")
      return 'finish'  
    
class Finish(Scene):

    def enter(self):
      print("\t\t\t\t          ---Finish--- ")
      print("\t\t\t   Thank you for playing Chronicles or Eternia")  