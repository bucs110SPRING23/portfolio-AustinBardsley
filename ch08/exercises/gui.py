class Goomba:
    def __init__(self,num=1):
        self.goomba_num = num
        self.is_alive = True
        self.is_moving = True
        self.collision = False

class MysteryBox:
    def __init__(self):
        self.contains_object = True
        self.object = "fire_flower_thing"
        self.object_collected = False

class Tube:
    def __init__(self,xcor,transport_location):
        self.pos = xcor
        self.can_transport = False #ie. if the player jumps
        self.where_to = transport_location


