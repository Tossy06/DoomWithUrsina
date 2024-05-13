from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Caja3D(Button):
    sprite_index="t.jpeg"
    
    def __init__(self,position = (0,0,0), escala=(0,0)):
        super().__init__(
            parent = scene,
            position=position,
            model='cube',
            origin_y=0.5,
            collider='box',
            texture=self.sprite_index,
            color=color.color(0,0,random.uniform(0.9,1)),
            scale=escala,
            highlight_color=color.lime )
jugador=FirstPersonController(position=(0,1,0))


class mano(Entity):
    xInicio=0 # Posición del arma en el eje X
    yInicio=-0.4 # Posición del arma en el eje Y
    image_speed=0.4
    image_index=0 # Imagen fija
    textura_mano=load_texture="we.png"
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='cube',
            texture=self.textura_mano,
            scale=0.4,
            color=color.white,
            rotation=Vec3(0,0,0), # girar el arma
            position=Vec2(self.xInicio,self.yInicio)
        )
arma= mano()

ground = Entity(model='plane', collider='box', scale=64, texture='lava2.jpg', texture_scale=(4,4))

# Creamos las paredes alrededor del suelo
wall_texture = load_texture('pared.jpg')  # Reemplaza 'wall_texture.png' con la ruta a tu textura de paredes

# Paredes alrededor del suelo
pared1 = Entity(model='cube', texture=wall_texture, scale=(ground.scale.x, 50, 1), position=(0, 0.5, ground.scale.z / 2))
pared1.collider = 'box'
pared2 = Entity(model='cube', texture=wall_texture, scale=(ground.scale.x, 50, 1), position=(0, 0.5, -ground.scale.z / 2))
pared2.collider = 'box'
pared3 = Entity(model='cube', texture=wall_texture, scale=(1, 50, ground.scale.z), position=(ground.scale.x / 2, 0.5, 0))
pared3.collider = 'box'
pared4 = Entity(model='cube', texture=wall_texture, scale=(1, 50, ground.scale.z), position=(-ground.scale.x / 2, 0.5, 0))
pared4.collider = 'box'

# Creamos las salas en las esquinas del plano
sala_texture = load_texture('sala.jpg')  # Reemplaza 'sala_texture.jpg' con la ruta a tu textura de sala

# Creamos las salas en las esquinas del plano
sala_texture = load_texture('sala.jpg')  # Reemplaza 'sala_texture.jpg' con la ruta a tu textura de sala
door_texture = load_texture('door_texture.jpg')  # Reemplaza 'door_texture.jpg' con la ruta a tu textura de puerta

# Creamos las salas
sala1 = Entity(model='cube', texture=sala_texture, scale=(30, 10, 30), position=(ground.scale.x / 2 - 15, 5, ground.scale.z / 2 - 15))
puerta1 = Entity(model='cube', texture=door_texture, scale=(1, 10, 5), position=(ground.scale.x / 2 - 15, 5, ground.scale.z / 2))
puerta2 = Entity(model='cube', texture=door_texture, scale=(1, 10, 5), position=(ground.scale.x / 2, 5, ground.scale.z / 2 - 15))

sala2 = Entity(model='cube', texture=sala_texture, scale=(30, 10, 30), position=(ground.scale.x / 2 - 15, 5, -ground.scale.z / 2 + 15))
puerta3 = Entity(model='cube', texture=door_texture, scale=(1, 10, 5), position=(ground.scale.x / 2 - 15, 5, -ground.scale.z / 2))
puerta4 = Entity(model='cube', texture=door_texture, scale=(1, 10, 5), position=(ground.scale.x / 2, 5, -ground.scale.z / 2 + 15))

sala3 = Entity(model='cube', texture=sala_texture, scale=(30, 10, 30), position=(-ground.scale.x / 2 + 15, 5, ground.scale.z / 2 - 15))
puerta5 = Entity(model='cube', texture=door_texture, scale=(1, 10, 5), position=(-ground.scale.x / 2, 5, ground.scale.z / 2 - 15))
puerta6 = Entity(model='cube', texture=door_texture, scale=(1, 10, 5), position=(-ground.scale.x / 2 + 15, 5, ground.scale.z / 2))

sala4 = Entity(model='cube', texture=sala_texture, scale=(30, 10, 30), position=(-ground.scale.x / 2 + 15, 5, -ground.scale.z / 2 + 15))
puerta7 = Entity(model='cube', texture=door_texture, scale=(1, 10, 5), position=(-ground.scale.x / 2, 5, -ground.scale.z / 2 + 15))
puerta8 = Entity(model='cube', texture=door_texture, scale=(1, 10, 5), position=(-ground.scale.x / 2 + 15, 5, -ground.scale.z / 2))



app.run()