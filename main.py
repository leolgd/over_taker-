import pygame
from pygame import mixer

from game import Game

pygame.init()
pygame.mixer.init(2)


if __name__ == "__main__":
    game = Game()
    game.run()