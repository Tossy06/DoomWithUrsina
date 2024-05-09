from ursina import *

from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = Entity(model='cube', color=color.orange, scale_y=2)

def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt
    
def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)
        


# start running the game
app.run()
