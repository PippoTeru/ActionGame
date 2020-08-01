# -*- coding: UTF-8 -*-

from Character.Character import Character
from .Event import Event
from .Move import Move
from .Animation import Animation


class Player(Character):
    def __init__(self, gameManager):
        super(Player, self).__init__(gameManager, "Character\Player\Data\Constants.json")

        self.isJump = {
            "init" : False,
            "rise" : False,
            "jumping" : False
        }

        self.event = Event(self)
        self.move = Move(self)
        self.animation = Animation(self)

    def update(self):
        self.judgmentIsGround()
        self.event.defineState()
        self.move.move()
        self.image = self.images[self.animation.getIndex()]
