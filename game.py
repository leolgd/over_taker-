import pygame

from screen import Screen
from player import Player
from map import Map

class Game:

  def __init__(self):
    self.running = True
    self.screen: Screen = Screen()
    self.map: Map = Map(self.screen)
    self.player: Player = Player
    self.screen = Screen()
    self.player = Player()


  def run(self):
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False


      self.player.move()
      self.player.draw()


      self.screen.update()