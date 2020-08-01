# -*- coding: UTF-8 -*-

from Character.Animation import Animation as characterAnimation

class Animation(characterAnimation):
    def __init__(self, player):
        super(Animation, self).__init__(player)

        self.__player = player

    def __getState(self):
        state = self.__player.event.getState()
        isSlip = self.__player.move.isSlip()
        direction = self.__player.move.getDirection()
        isJump = self.__player.isJump

        if state == 1:
            if isSlip == 2:
                self.__state = self.__data["leftLookBack"]
            else:
                self.__state = self.__data["rightWalk"]
        elif state == 2:
            if isSlip == 1:
                self.__state = self.__data["rightLookBack"]
            else:
                self.__state = self.__data["leftWalk"]
        else:
            if direction == 1:
                if isSlip == 1:
                    self.__state = self.__data["rightSlip"]
                elif isSlip == 0:
                    self.__state = self.__data["rightIdle"]
            else:
                if isSlip == 2:
                    self.__state = self.__data["leftSlip"]
                elif isSlip == 0:
                    self.__state = self.__data["leftIdle"]

        if isJump["jumping"]:
            if direction == 1:
                self.__state = self.__data["rightJump"]
            else:
                self.__state = self.__data["leftJump"]
