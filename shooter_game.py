#Создай собственный Шутер

import pygame as pg

pg.init()
pg.mixer.init()
class GameSprite(pg.sprite.Sprite):
    def __init__(self, filename, x, y, width, height, speed):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self):
        window.blit(self.image, self.rect)


W, H = (700, 500)
FPS = 120
clock = pg.time.Clock()
pg.mixer.music.load('space.ogg')
pg.mixer.music.play()