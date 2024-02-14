import pygame
from screen import Screen

class Player(pygame.sprite.Sprite):

  def __init__(self):

    super().__init__()  

    ########## Images du joueur ##########
    self.sprite_load = pygame.image.load('assets/sprite/sprite_pokemon.png').convert_alpha()
    self.sprites = []
    x,y = 4,4
    for y_coordinate in range(4):
      for x_coordinate in range(4):
        self.sprites.append(self.sprite_load.subsurface(x, y, 18, 27))
        x += 18+7
      x = 4
      y += 27+4
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]
    self.rect = self.image.get_rect()
    self.rect.x, self.rect.y = 250, 250
    self.zoom = 4
    self.size_x, self.size_y = self.image.get_width(), self.image.get_height()

    ########## Caractéristique du joueur ##########
    self.pseudo = "Sika"
    self.speed = 1
    self.animation_speed = 0.05


  """def update(self):
    self.current_sprite += self.animation_speed

    if self.current_sprite >= len(self.sprites):
      self.current_sprite = 0

    self.image = self.sprites[int(self.current_sprite)]"""


  def up_animation(self):
    if self.current_sprite < 12:
      self.current_sprite = 12
    self.image = self.sprites[int(self.current_sprite)] 
    self.current_sprite += self.animation_speed
    if self.current_sprite >= 15:
      self.current_sprite = 12

    
  def down_animation(self):
    if self.current_sprite > 3:
      self.current_sprite = 0   
    self.image = self.sprites[int(self.current_sprite)]
    self.current_sprite += self.animation_speed
    if self.current_sprite >= 3:
      self.current_sprite = 0


  def right_animation(self):
    if self.current_sprite < 8 or self.current_sprite > 11:
      self.current_sprite = 8
    self.image = self.sprites[int(self.current_sprite)]
    self.current_sprite += self.animation_speed
    if self.current_sprite >= 11:
      self.current_sprite = 8


  def left_animation(self):
    if self.current_sprite < 4 or self.current_sprite > 7:
      self.current_sprite = 4
    self.image = self.sprites[int(self.current_sprite)]
    self.current_sprite += self.animation_speed
    if self.current_sprite >= 7:
      self.current_sprite = 4


  def draw(self): # Met sur l'écran l'image du joueur
    Screen.display.blit(pygame.transform.scale(self.image, (self.zoom * self.size_x, self.zoom * self.size_y)), self.rect)


  def move(self): # Permet au joueur de se déplacer

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_q] and not keys[pygame.K_UP] and not keys[pygame.K_z] and not keys[pygame.K_DOWN] and not keys[pygame.K_s]:
      self.rect.x -= self.speed
      self.left_animation()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and not keys[pygame.K_UP] and not keys[pygame.K_z] and not keys[pygame.K_DOWN] and not keys[pygame.K_s]:
      self.rect.x += self.speed
      self.right_animation() 

    if keys[pygame.K_UP] or keys[pygame.K_z] and not keys[pygame.K_RIGHT] and not keys[pygame.K_d] and not  keys[pygame.K_LEFT] and not keys[pygame.K_q]:
      self.rect.y -= self.speed
      self.up_animation()

    if keys[pygame.K_DOWN] or keys[pygame.K_s] and not keys[pygame.K_RIGHT] and not keys[pygame.K_d] and not  keys[pygame.K_LEFT] and not keys[pygame.K_q]:
      self.rect.y += self.speed
      self.down_animation()

    if (keys[pygame.K_UP] or keys[pygame.K_z]) and (keys[pygame.K_LEFT] or keys[pygame.K_q]):
      self.rect.x -= self.speed * 0.707
      self.rect.y -= self.speed * 0.707
      self.up_animation()

    if (keys[pygame.K_UP] or keys[pygame.K_z]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
      self.rect.x += self.speed * 0.707
      self.rect.y -= self.speed * 0.707
      self.up_animation()
    
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (keys[pygame.K_LEFT] or keys[pygame.K_q]):
      self.rect.x -= self.speed * 0.707
      self.rect.y += self.speed * 0.707
      self.down_animation()

    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
      self.rect.x += self.speed * 0.707
      self.rect.y += self.speed * 0.707
      self.down_animation()