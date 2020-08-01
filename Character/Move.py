# -*- coding: UTF-8 -*-

class Move:
    def __init__(self, character):
        self.__character = character

        self.__horizontalVelocity = 0
        self.__horizontalPhysicalData = self.__character.constants["horizontalPhysicalData"]
        self.__horizontalVelocityLimit = self.__horizontalPhysicalData["velocityLimit"]
        self.__horizontalStartingAcceleration = self.__horizontalPhysicalData["startingAcceleration"]
        self.__horizontalStoppingAcceleration = self.__horizontalPhysicalData["stoppingAcceleration"]

        self.__verticalVelocity = 0
        self.__verticalPhysicalData = self.__character.constants["verticalPhysicalData"]
        self.__fallVelocityLimit = self.__verticalPhysicalData["fallVelocityLimit"]
        self.__fallAcceleration = self.__verticalPhysicalData["fallAcceleration"]

        self.__direction = 1

    def __moveX(self):
        state = self.__character.event.getState()

        if state == 0:
            self.__stop()
        elif state == 1:
            if self.__horizontalVelocity < 0:
                self.__stop()
            else:
                self.__direction = 1
                self.__walk()
        elif state == 2:
            if self.__horizontalVelocity > 0:
                self.__stop()
            else:
                self.__direction = -1
                self.__walk()

        self.__character.x += self.__horizontalVelocity
        self.__character.x = min(max(self.__character.x, 0), 736)

    def __stop(self):
        if self.__horizontalVelocity > 0:
            self.__horizontalVelocity += self.__horizontalStoppingAcceleration
        elif self.__horizontalVelocity < 0:
            self.__horizontalVelocity += -self.__horizontalStoppingAcceleration
        else:
            self.__horizontalVelocity = 0

    def __walk(self):
        if abs(self.__horizontalVelocity) < self.__horizontalVelocityLimit:
            self.__horizontalVelocity += self.__horizontalStartingAcceleration * self.__direction
        else:
            self.__horizontalVelocity = self.__horizontalVelocityLimit * self.__direction

    def __moveY(self):
        self.__fall()

        self.__character.y += self.__verticalVelocity
        self.__character.y = min(self.__character.y, 536)

    def __fall(self):
        if self.__verticalVelocity < self.__fallVelocityLimit:
            self.__verticalVelocity += self.__fallAcceleration
        else:
            self.__verticalVelocity = self.__fallVelocityLimit

    def move(self):
        self.__moveX()
        self.__moveY()

    def getDirection(self):
        return self.__direction
