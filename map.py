import pygame
import pytmx
import pyscroll

from screen import Screen
from player import Player

class Map:
     def __init__(self, screen: Screen):
        self.screen: Screen = screen
        self.switch_map("map_0")
        self.player: Player | None = None

     def switch_map(self, map: str) -> None:
        self.tmx_data = pytmx.load_pygame(f"assets/map/grotte/{map}.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 3

     def add_player(self, player) -> None:
        self.group.add(player)
        self.player = player


     def update(self) -> None:
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())