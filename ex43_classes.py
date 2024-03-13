'''
aliens have invaded a space ship and our hero has to go through
a maze of rooms defeating them so he can escape into an escape
pod to the planet below. the game will be more like a zork or
adventure type game with text outputs and funny ways to die. the
game will involve an engine that runs a map full of rooms or scenes.
each room will print its own description when the player enters
it and then tell the engine what room to run next out of the map.


*** SCENES ***
death: this is when the player dies and should be something funny

central corridor: starting point and has a gothon already standing
    there that the players have to defeat with a joke before
    continuing

laser weapon armory: where the hero gets a neutron bomb to blow up
    the ship before getting to the escape pod. it has a keypad the
    hero has to guess the number for

the bridge: another battle scene with a gothon where the hero
    places the bomb

escape pod: where the hero escapes but only after guessing the right
    escape pod


*** NOUNS ***
- alien
- player
- ship
- maze
- room
- scene
- gothon
- escape pod
- planet
- map
- engine
- death
- central corridor
- laser weapon armory
- the bridge


*** CLASS HIERARCHY & ACTIONS/VERBS/FUNCTIONS ***
- map
    > next_scene
    > opening_scene
- engine
    > play
- scene
    > enter
    - death
    - central corridor
    - laser weapon armory
    - the bridge
    - escape pod
'''
from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]
    
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving member
            and your last mission is to get the neutron destruction bomb
            from the Weapons Armory, put it in the bridge, and blow up
            the ship after getting into an escape pod.
                     
            You're running down the central corridor to the Weapons Armory
            when a Gothon jumps out, red scaly skin, dark grimy teeth,
            and evil clown costume flowing around his hate filled body.
            He's blocking the door to the Armory and about to pull a weapon
            to blast you.
            """))
        
        action = input("> ")

        if action == "shoot!":
            print(dedent(
                """
                Quick on the draw you yank out your blaster and fire it at
                the Gothon. His clown costume is flowing and moving around
                his body, which throws off your aim. Your laser hits his costume
                but misses him entirely. This completely ruins his brand new
                costume his mother bought him, which makes him fly into an 
                insane rage and blast you repeatedly in the face until
                you are dead. Then he eats you
                """
            ))  
            return 'death'
        
        elif action == "dodge!":
            print(dedent(
                """
                You dodge but your foot slips and you fall.
                He gets you then he eats you and you die.
                """
            ))  
            return 'death'
        
        elif action == "tell a joke":
            print(dedent(
                """
                He likes your jokes and cant control his laugh.
                While he stops moving, you shoot him in the head and
                go to the armory.
                """
            ))  
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent(
                """
                You find the bomb in its container which has a keypad.
                Get the code wrong 10 times and it locks forever and
                you fail. It's a 3 digit code.
                """
            ))
        
        code = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZ")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent(
                """
                The container opens, you grab the bomb, and run to 
                the bridge
                """
            ))
            return 'the_bridge'
        else:
            print(dedent(
                """
                The box is permanently locked and you have no escape.
                You shoot yourself in the head.
                """
            ))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent(
                """
                You get to the bridge and find 5 Gothons. They dont shoot you
                immediately seeing that you have the bomb in your hands
                """
            ))
        
        action = input("> ")

        if action == "throw the bomb":
            print(dedent(
                """
                It explodes on impact and kills everyone
                """
            ))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent(
                """
                You plant the bomb while pointing your gun at the Gothons.
                You run to the next room where the escape pods are
                """
            ))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class EscapePod(Scene):

    def enter(self):
        print(dedent(
                """
                There are 5 escape pods and some could be damaged. You need to
                choose the 1 good pod to escape, otherwise you will die.
                """
            ))
        
        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(
                f"""
                You get into pod {guess} and it implodes upon ejection. You die. 
                """
            ))
            return 'death'
        else:
            print(dedent(
                f"""
                {guess} is the good pod and you escape with your life
                """
            ))
            return 'finished'
        
class Finished(Scene):

    def enter(self):
        print("You won")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
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