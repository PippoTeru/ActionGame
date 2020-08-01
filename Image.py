# -*- Coding: UTF-8 -*-

import pygame
from pygame.locals import *


def loadImage(path):
    image = pygame.image.load(path)
    image.convert_alpha()

    return image


def splitImage(images, length):
    imageList = []

    imagesWidth = images.get_width()
    imageWidth = int(imagesWidth / length)
    imageHeight = images.get_height()

    baseImage = pygame.Surface((imageWidth, imageHeight))

    for i in range(0, imagesWidth, imageWidth):
        image = baseImage.copy()
        image.blit(images, (-i, 0))
        image.set_colorkey(Color("#FF00FF"), RLEACCEL)
        image.convert()
        imageList.append(image)

    return imageList


def flipImage(chipList):
    for i in range(len(chipList)):
        chipList.append(pygame.transform.flip(chipList[i], True, False))

    return chipList
