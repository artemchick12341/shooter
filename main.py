#Создай собственный Шутер

import pygame as pg
import pygame_menu
import random

pg.init()
pg.mixer.init()
pg.font.init()
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
class Player(GameSprite):
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT] and self.rect.right < W:
            self.rect.x += self.speed
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 20, 30, 10)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= H:
            self.rect.y = random.randint(-150, -50)
            self.rect.x = random.randint(0, W)
            self.speed = random.choice(speeds)
            start_menu()
            
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            self.kill()
        
            


W, H = (1920, 1080)
FPS = 120
clock = pg.time.Clock()
pg.mixer.music.load('space.ogg')
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play()

BACK_IMAGE = pg.transform.scale(pg.image.load('galaxy.jpg'), (W, H))
BLACK = (0, 255, 0)
window = pg.display.set_mode((W, H))
pg.display.set_caption('Шутер')
rocket = Player('rocket.png', 120, H - 120, 90, 120, 5)
speeds = [0.2, 0.5, 1, 1.2, 1.5, 1.7, 2]
ufos = pg.sprite.Group()
bullets = pg.sprite.Group()
fsize = 20
font = pg.font.SysFont('Arial', fsize)
text = font.render('Счёт: 0', True, BLACK)




def main(difficulty):
    score = 0
    font = pg.font.SysFont('Arial', 60)
    text = font.render('Счёт: 0', True, BLACK)
    ufos.empty()
    ufos.add(
    Enemy('ufo.png', random.randint(0, W), random.randint(-100, -50), 90, 80, random.choice(speeds)),
    Enemy('ufo.png', random.randint(0, W), random.randint(-100, -50), 90, 80, random.choice(speeds)),
    Enemy('ufo.png', random.randint(0, W), random.randint(-100, -50), 90, 80, random.choice(speeds)),
    Enemy('ufo.png', random.randint(0, W), random.randint(-100, -50), 90, 80, random.choice(speeds)),
    Enemy('ufo.png', random.randint(0, W), random.randint(-100, -50), 90, 80, random.choice(speeds)),
    )
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    rocket.fire()
        collides = pg.sprite.groupcollide(bullets, ufos, True, True)
        for _ in collides:
            ufo = Enemy('ufo.png', random.randint(0, W), random.randint(-100, -50), 90, 80, random.choice(speeds))
            ufos.add(ufo)
            score += 1
            text = font.render('Счёт:' + str(score), True, BLACK)
        if score == 20 and difficulty == True:
            difficulty == False
        window.blit(BACK_IMAGE ,(0, 0))
        window.blit(text, (W - 300, 50))
        rocket.draw()
        rocket.update()
        bullets.draw(window)
        bullets.update()
        ufos.draw(window)
        ufos.update()
        if difficulty == True:
            pg.display.update()
            clock.tick(FPS)
        else:
            font2 = pg.font.SysFont('Arial', 150)
            text = font2.render('Ты победил!', True, BLACK)

def start_menu():
    menu = pygame_menu.Menu('Шутер', 400, 200, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Играть', main(True))
    menu.add.selector('Выберите режим игры:', [('Обычный', 1), ('Бесконечный', 2)])
    menu.add.button('Выйти из игры', pygame_menu.events.EXIT)
    menu.mainloop(window)

if __name__ == '__main__':
    start_menu()
