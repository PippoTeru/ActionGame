# -*- coding: UTF-8 -*-

class Animation:
    def __init__(self, character):
        self.__character = character

        self.__data = self.__character.constants["animationData"]

        self.__state = None

    def __getState(self):
        state = self.__character.event.getState()
        isSlip = self.__character.move.isSlip()
        direction = self.__character.move.getDirection()
        isJump = self.__character.isJump

        if state == 1:
            self.__state = self.__data["rightWalk"]
        elif state == 2:
            self.__state = self.__data["leftWalk"]

    def getIndex(self):
        self.__getState()

        times = self.__state[0]
        locate = self.__state[1]
        animationCycle = self.__state[2]

        frame = self.__character.gameManager.frame

        index = locate if animationCycle is None else int(frame / animationCycle % times) + locate

        return index
