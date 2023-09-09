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
      As you make your way across the Golden Plain, you get surrounded by the Fallen with their
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
            Using this opportunity you run towards Dragonkeep Mountain.
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
      print("-" * 90)
      print(dedent("""
      You look around to see where you have been teleported and find yourself in the throne room of the humans. The kings gurads
      draw their sword and seem to be demanding a surrender. 

      Press 1: Draw you bow

      Press 2: Raise your hands up to surrender
      """))
      while True:
         action = input("< ")
         print("-" * 90)
         if action == "1":
            print(dedent("""
            You draw your bow and get ready to fight. However in a flash you see the world turn upside down and you body with the bow still drawn.
            """))
            return 'death'
         elif action == "2":
            print(dedent("""
            You surrender and the gurads put you in a shackle. They bring you infront of the king. As they bring yo uto the key the Eternia Crystal 
            and the Kings Crown starts to shine brightly. Using this oppurtunity of the light you run out of the throne room and come across stairs.
            """))
            break
         else:
            print("Please select action")
      print(dedent("""
      Press 1: Go up

      Press 2: Go down
      """))  
      while True:
         action = input("< ")
         print("-" * 90)
         if action == "1":
            print("You run up the stairs and end up on the top of the castle. With nowhere to run the guards surround you and stab you to death.")
            return 'death'
         elif action == "2":
            print(dedent("""
            You run down into the basement and come across the same engraving of the dragon as last time. The Eternia Crystal shines along with the dragon
            eye. You then teleport out of the Kingdom.
            """))
            return 'f_dungeon'
         else:
            print("Input action")
    
class FinalDungeon(Scene):

    def enter(self):
      print("\t\t\t\t     ---Zephyrs Dungeon---")
      print(dedent("""
      The Kingdoms basement were replaced by gloomy labrynth stone, where eerie shadows danced and whispered along the walls. The scent of 
      moss and dampness assaulted your senses. As you cautiously make your way through the dimly lit corridors, you pick up faint sounds of
      footsteps. You hide behind the walls and discover that the Fallen are also in the dungeon. You traverse deeper into the dungeon and 
      you come across a large door similar to the door of the ruins. However, there are the Fallen guarding the doors.

      Press 1: Sneak attack

      Press 2: Create a distraction to slip past the Fallen

      """))
      
      while True:
         action = input("< ")
         print("-" * 90)
         if action == "1":
            print(dedent("""
            You go along the walls and prepare to shoot two arrows for the two Fallen standing guard. You let the arrows fly and hit both of them.
            """))
            break
         elif action == "2":
            print(dedent("""
            You get ready to throw a stone to distract the but as you throw the stone you throw it near you. The Fallen turns towards you and sees you.
            They sound the alarm and you get surrounded by hundreds of Fallen instantly. A barrgae of arrows from the Fallen come down on you.
            """))
            return 'death'
         else:
            print("Correct Input ")
      if fragment == 1:
        print(dedent("""
        You head to the door and the Eternia Crystal shines brightly as it floats away from you it enters an engraving on the door. The door then opens 
        and teleports you away.
        """))
        return 'f_room'
      else:
        print("The Eternia Crystal lights up then falls into pieces the door opens up and teleports you away")
        return 'death'
    
class FinalRoom(Scene):

    def enter(self):
      print("\t\t\t\t     ---The Throne Room---")
      print(dedent("""
      You appear at an ancient throne room with at the very center a bow with a carving of a dragon. You pick up the bow and feel a surge of power. 
      Then a voice comes into your head.
      'Only those worthy can use the bow prove your worth by answering thy riddle. 
        I am the beginning of eternity,
        The end of time and space,
        The beginning of every end,
        And the end of every place.

        What am I?

      """))
      action = input("< ")
      print("-" * 90)
      if action.upper() == "E":
         print("You are worthy of possesing the bow of Yggdrasil. Use it to protect what yo most desire")
         return 'forest'
      else:
         print("You are unworthy of the bow. Those unworthy must be put to rest")
         return 'death'

class Forest(Scene):

    def enter(self):
      print("\t\t\t\t       ---Elven Forest---")
      print(dedent("""
      You get transported to the Forest and see it run over by the Fallen. You draw the great bow and release an energy beam that cleanses the forest of all evil.
      """))
      return 'finish'  
    
class Finish(Scene):

    def enter(self):
      print("\t\t\t\t          ---Finish--- ")
      print("\t\t\t   Thank you for playing Chronicles or Eternia")  