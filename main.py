# Main file running the game
import game_scenes

class Engine(object):
  def __init__(self, scene_map):
    self.scene_map = scene_map
  def play(self):
    current_scene = self.scene_map.opening_scene()
    last_scene = self.scene_map.next_scene('finish')

    while current_scene != last_scene:
      next_scene_name = current_scene.enter()
      current_scene = self.scene_map.next_scene(next_scene_name)

    current_scene.enter()

class Map(object):
  scenes = {
    'start': game_scenes.StartingScreen(),
    'death': game_scenes.Death(),
    'begin': game_scenes.Beginning(),
    'forest': game_scenes.Forest(),
    'plain': game_scenes.Plains(),
    'mountain': game_scenes.Mountain(),
    'm_ruin': game_scenes.MountainRuins(),
    'kingdom': game_scenes.Kingdom(),
    'f_dungeon': game_scenes.FinalDungeon(),
    'f_room': game_scenes.FinalRoom(),
    'finish': game_scenes.Finish()
  }
  def __init__(self,start_scene):
    self.start_scene = start_scene

  def next_scene(self, scene_name):
    val = Map.scenes.get(scene_name)
    return val

  def opening_scene(self):
    return self.next_scene(self.start_scene)

start_map = Map('start')
start_game = Engine(start_map)
start_game.play()