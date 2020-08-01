# -*- coding: UTF-8 -*-

from Character.Move import Move as characterMove


class Move(characterMove):
    def __init__(self, player):
        super(Move, self).__init__(player)

        self.__player = player

        self.__verticalPhysicalData = self.__player.constants["verticalPhysicalData"]
        self.__riseInitialVelocity = self.__verticalPhysicalData["riseInitialVelocity"]
        self.__riseAcceleration = self.__verticalPhysicalData["riseAcceleration"]

    def __moveY(self):
        if self.__player.isJump["init"] or self.__player.isJump["rise"]:
            self.__jump()
        else:
            self.__fall()

        self.__player.y += self.__verticalVelocity
        self.__player.y = min(self.__player.y, 536)

        if self.__player.y == 536:
            self.__player.isJump["jumping"] = False

    def __jump(self):
        if self.__player.isJump["init"]:
            self.__verticalVelocity = self.__riseInitialVelocity
            self.__player.isJump["init"] = False
            self.__player.isJump["rise"] = True
        if self.__player.event.getKeyEvent() in (4, 5, 6):
            self.__verticalVelocity += self.__riseAcceleration
            if self.__verticalVelocity >= 0:
                self.__verticalVelocity = 0
                self.__player.isJump["rise"] = False
        else:
            self.__player.isJump["rise"] = False

    def isSlip(self):
        if self.__horizontalVelocity > 0:
            return 1
        elif self.__horizontalVelocity < 0:
            return 2
        else:
            return 0
