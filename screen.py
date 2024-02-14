import pygame

class Screen:

  display = pygame.display.set_mode((0, 0))

  def __init__(self):
    pygame.display.set_caption("Overtaker")
    self.clock = pygame.time.Clock()
    self.framerate = 144

  def update(self):
    pygame.display.flip()
    pygame.display.update()
    self.clock.tick(self.framerate)
    self.display.fill((0, 0, 0))