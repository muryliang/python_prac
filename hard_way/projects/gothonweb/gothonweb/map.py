class Room(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}

	def go(self, direction):
                if self.paths.get(direction, None) == None:
                    if self.paths.get('*', None) != None :
                        return self.paths.get('*')
                    else:
                        return None
                return self.paths.get(direction)
                    

	def add_paths(self, paths):
		self.paths.update(paths)

central_corridor = Room("Central Corrodir", "this is the central_corridor")
laser_weapon_armory = Room("Laser Weapon Armony", "laser_weapon_armory")
the_bridge = Room("The Bridge", "the_bridge")
escape_pod = Room("Escape Pod", "escape_pod")
the_end_winner = Room("The End win", "the_end win")
the_end_loser = Room("The End lose", "the_end lose")

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser,
    })

generic_death = Room("Death", "dead")

generic_death.add_paths({
    '*':generic_death,
    })

the_bridge.add_paths({
    'throw the bomb':generic_death,
    'slowly place the bomb': escape_pod,
    '*':generic_death,
    })

laser_weapon_armory.add_paths({
    '0132':the_bridge,
    '*':generic_death,
    })

central_corridor.add_paths({
    'shoot':generic_death,
    'dodge!':generic_death,
    'tell a joke': laser_weapon_armory
    })

START = central_corridor
