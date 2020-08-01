# -*- coding: UTF-8 -*-

import json

import pygame

import Image
from .Move import Move
from .Animation import Animation


class Character(pygame.sprite.Sprite):
    def __init__(self, gameManager, jsonFilePath):
        self.gameManager = gameManager

        self.constants = self.__loadJson(jsonFilePath)

        self.__imageData = self.constants["imageData"]
        self.images = self.__getImage()
        self.image = self.images[0]

        self.__initialPositionData = self.constants["initialPositionData"]
        self.x = self.__initialPositionData["x"]
        self.y = self.__initialPositionData["y"]
        self.__rect = self.image.get_rect(left=self.x, top=self.y)

        self.isGround = True

        self.move = Move(self)
        self.animation = Animation(self)

    def __loadJson(self, path):
        file = open(path, "r")

        return json.load(file)

    def __getImage(self):
        baseImage = Image.loadImage(self.__imageData["path"])
        imageList = Image.splitImage(baseImage, self.__imageData["length"])

        return Image.flipImage(imageList)

    def judgmentIsGround(self):
        if self.y == 536:
            self.isGround = True
        else:
            self.isGround = False

    def update(self):
        self.judgmentIsGround()
        self.move.move()
        self.image = self.images[self.animation.getIndex()]

    def draw(self):
        self.gameManager.screen.blit(self.image, (self.x, self.y))
