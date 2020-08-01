# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *


class Event:
    def __init__(self, player):
        self.__player = player

        self.__keyEvent = 0
        self.__previousKeyEvent = 0

        self.__state = 0

    def __defineKeyEvent(self):
        keyPressed = pygame.key.get_pressed()

        self.__previousKeyEvent = self.__keyEvent
        self.__keyEvent = 0

        keys = [K_RIGHT, K_LEFT, K_SPACE]

        for i in range(len(keys)):
            if keyPressed[keys[i]]:
                self.__keyEvent += 2 ** i

    def __stateMachine(self):
        isGround = self.__player.isGround

        if self.__keyEvent == 1:
            self.__state = 1
        elif self.__keyEvent == 2:
            self.__state = 2
        elif self.__keyEvent == 4:
            if self.__previousKeyEvent == 0:
                if self.__player.isJump["jumping"] is False and isGround:
                    self.__player.isJump["init"] = True
                    self.__player.isJump["jumping"] = True
        elif self.__keyEvent == 5:
            self.__state = 1
            if self.__previousKeyEvent == 1:
                if self.__player.isJump["jumping"] is False and isGround:
                    self.__player.isJump["init"] = True
                    self.__player.isJump["jumping"] = True
        elif self.__keyEvent == 6:
            self.__state = 2
            if self.__previousKeyEvent == 2:
                if self.__player.isJump["jumping"] is False and isGround:
                    self.__player.isJump["init"] = True
                    self.__player.isJump["jumping"] = True
        else:
            self.__state = 0

    def defineState(self):
        self.__defineKeyEvent()
        self.__stateMachine()

    def getState(self):
        return self.__state

    def getKeyEvent(self):
        return self.__keyEvent
