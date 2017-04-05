# -*- coding: utf-8 -*-

from sys import exit
from random import randint
class Scene(object):

    def enter(self):
        print "this should never be called"
        exit(0)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('Finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            print 'next scene name is', next_scene_name
        current_scene.enter()

class Death(Scene):
    def enter(self):
        print "you are dead"
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print "now in CentralCorridor"
        return 'LaserWeaponArmory'

class LaserWeaponArmory(Scene):
    def enter(self):
        print "now in LaserWeaponArmory"
        return 'TheBridge'

class TheBridge(Scene):
    def enter(self):
        print "now in TheBridge"
        return 'EscapePod'

class EscapePod(Scene):
    def enter(self):
        print "now in EscapePod"
        return 'Finished'

class Finished(Scene):
    def enter(self):
        print 'You win!!'
        return 'Finished'

class Map(object):
    scenes = {
            'central_corridor':CentralCorridor(),
            'LaserWeaponArmory':LaserWeaponArmory(),
            'TheBridge': TheBridge(),
            'EscapePod':EscapePod(),
            'Death':Death(),
            'Finished':Finished(),
            }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
