# -*- Coding: UTF-8 -*-

import pygame
from pygame.locals import *
import sys

from Character.Player.Player import Player


class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

        self.__player = Player(self)

        self.frame = 0
        self.__clock = pygame.time.Clock()

    def process(self):
        self.__quit()

        self.screen.fill(Color("#000000"))

        self.__update()
        self.__draw()

        self.frame += 1

        self.__clock.tick(60)

    def __quit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


    def __update(self):
        self.__player.update()

    def __draw(self):
        self.__player.draw()

        pygame.display.update()
