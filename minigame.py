import pygame

pygame.init()
window = pygame.display.set_mode((1535, 800))
window.fill((22, 43, 66))
pygame.display.set_caption('Лабіринт')


class Pic(pygame.sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Pic):
    def __init__(self, picture, w, h, x, y, speed_x=0, speed_y=0):
        super().__init__(picture, w, h, x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 800:
            self.rect.bottom = 800
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 1535:
            self.rect.right = 1535
        self.rect.x += self.speed_x
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
        if self.speed_x > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        if self.speed_x < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)

        self.rect.y += self.speed_y
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
        if self.speed_y < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        elif self.speed_y > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)

    def fire(self):
        bul = Bullet('bullet.png', 20, 10, self.rect.right - 30, self.rect.centery, 10)
        bullets.add(bul)

    def fire_left(self):
        bul2 = Bullet1('bullet.png', 20, 10, self.rect.left - 30, self.rect.centery, 10)
        bullets.add(bul2)


class Enemy(Pic):
    def __init__(self, picture, w, h, x, y, speed, x_min, x_max):
        super().__init__(picture, w, h, x, y)
        self.speed = speed
        self.x_min = x_min
        self.x_max = x_max
        self.direction = 'left'

    def update(self):
        if self.rect.x >= self.x_max:
            self.direction = 'left'
        if self.rect.x <= self.x_min:
            self.direction = 'right'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Enemy1(Pic):
    def __init__(self, picture, w, h, x, y, speed_y, y_min, y_max):
        super().__init__(picture, w, h, x, y)
        self.speed_y = speed_y
        self.y_min = y_min
        self.y_max = y_max
        self.direction = 'up'

    def update(self):
        if self.rect.y >= self.y_max:
            self.direction = 'up'
        if self.rect.y <= self.y_min:
            self.direction = 'down'
        if self.direction == 'up':
            self.rect.y -= self.speed_y
        else:
            self.rect.y += self.speed_y


class Enemy2(Pic):
    def __init__(self, picture, w, h, x, y, speed_xy):
        super().__init__(picture, w, h, x, y)
        self.speed_xy = speed_xy
        self.direction = 'right'

    def update(self):
        if self.rect.x == 1150 and self.rect.y == 420:
            self.direction = 'right'
        elif self.rect.x == 1450 and self.rect.y == 420:
            self.direction = 'up'
        elif self.rect.x == 1450 and self.rect.y == 250:
            self.direction = 'left'
        elif self.rect.x == 1150 and self.rect.y == 250:
            self.direction = 'down'
        if self.direction == 'right':
            self.rect.x += self.speed_xy
        elif self.direction == 'left':
            self.rect.x -= self.speed_xy
        elif self.direction == 'up':
            self.rect.y -= self.speed_xy
        else:
            self.rect.y += self.speed_xy


class Enemy3(Pic):
    def __init__(self, picture, w, h, x, y, life):
        super().__init__(picture, w, h, x, y)
        self.life = life

    def fire(self):
        bul1 = Bullet('bullet.png', 20, 10, 50, 350, 10)
        bullets2.add(bul1)

    def fire_left(self):
        bul3 = Bullet1('bullet.png', 20, 10, 1235, 50, 10)
        bullets2.add(bul3)


class Bullet(Pic):
    def __init__(self, picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 1535:
            self.kill()


class Bullet1(Pic):
    def __init__(self, picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()


class Boost(Pic):
    def __init__(self, picture, w, h, x, y, speed_plus=3):
        super().__init__(picture, w, h, x, y)
        self.speed_plus = speed_plus

    def booster(self):
        self.kill()


main_player = Player('hero.png', 55, 55, 50, 700)

# v
player_v1 = Pic('platform2_v.png', 30, 165, 880, 245)
player_v2 = Pic('platform2_v.png', 30, 250, 440, 550)
player_v3 = Pic('platform2_v.png', 30, 240, 660, 420)
player_v4 = Pic('platform2_v.png', 30, 115, 1100, 405)
player_v5 = Pic('platform2_v.png', 30, 230, 880, 560)
player_v6 = Pic('platform2_v.png', 30, 140, 1100, 650)
player_v7 = Pic('platform2_v.png', 30, 110, 1100, 105)
player_v8 = Pic('platform2_v.png', 30, 200, 660, 110)
player_v10 = Pic('platform2_v.png', 30, 200, 440, 0)
player_v11 = Pic('platform2_v.png', 30, 230, 220, 70)
player_v12 = Pic('platform2_v.png', 30, 100, 1315, 0)

# g
player_g1 = Pic('platform2.png', 240, 30, 230, 540)
player_g2 = Pic('platform2.png', 200, 30, 0, 650)
player_g3 = Pic('platform2.png', 1155, 30, -30, 400)
player_g4 = Pic('platform2.png', 220, 30, 1100, 650)
player_g5 = Pic('platform2.png', 220, 30, 1315, 500)
player_g7 = Pic('platform2.png', 440, 30, 1100, 200)
player_g8 = Pic('platform2.png', 468, 30, 660, 100)
player_g9 = Pic('platform2.png', 200, 30, 470, 282)
player_g10 = Pic('platform2.png', 220, 30, 230, 170)

final = Pic('pac-1.png', 90, 90, 1400, 30)
x2speed = Boost('spe.png', 90, 90, 1400, 660)
win = Pic('thumb.jpg', 1535, 800, 0, 0)
lose = Pic('replay.png', 200, 200, 667, 300)

enemy = Enemy3('cyborg.png', 50, 50, 0, 330, True)
enemy1 = Enemy3('cyborg.png', 50, 50, 1250, 30, True)
enemies3 = pygame.sprite.Group()
enemies3.add(enemy)
enemies3.add(enemy1)

enemy_xy = Enemy2('cyborg.png', 50, 50, 1150, 420, 5)
enemies_xy = pygame.sprite.Group()
enemies_xy.add(enemy_xy)

enemy_y1 = Enemy1('cyborg.png', 50, 50, 750, 550, 5, 450, 720)

enemies_y = pygame.sprite.Group()
enemies_y.add(enemy_y1)

enemy_x1 = Enemy('cyborg.png', 50, 50, 10, 460, 5, 10, 600)
enemy_x2 = Enemy('cyborg.png', 50, 50, 900, 560, 5, 910, 1500)

enemies = pygame.sprite.Group()
enemies.add(enemy_x1)
enemies.add(enemy_x2)

boosters = pygame.sprite.Group()
boosters.add(x2speed)

barriers = pygame.sprite.Group()

barriers.add(player_g1)
barriers.add(player_g2)
barriers.add(player_g3)
barriers.add(player_g4)
barriers.add(player_g5)
barriers.add(player_g7)
barriers.add(player_g8)
barriers.add(player_g9)
barriers.add(player_g10)

barriers.add(player_v1)
barriers.add(player_v2)
barriers.add(player_v3)
barriers.add(player_v4)
barriers.add(player_v5)
barriers.add(player_v6)
barriers.add(player_v7)
barriers.add(player_v8)
barriers.add(player_v10)
barriers.add(player_v11)
barriers.add(player_v12)

bullets = pygame.sprite.Group()

bullets2 = pygame.sprite.Group()

clock = pygame.time.Clock()
speed_const_x = 5
speed_const_y = -5

run = True
finish = False
enemy_fire = 0
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_player.speed_y = speed_const_y
            elif event.key == pygame.K_DOWN:
                main_player.speed_y = speed_const_x
            elif event.key == pygame.K_LEFT:
                main_player.speed_x = speed_const_y
            elif event.key == pygame.K_RIGHT:
                main_player.speed_x = speed_const_x
            elif event.key == pygame.K_w:
                main_player.fire()
            elif event.key == pygame.K_q:
                main_player.fire_left()
            elif event.key == pygame.K_SPACE and finish:
                main_player.rect.x = 50
                main_player.rect.y = 700
                finish = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                main_player.speed_y = 0
            elif event.key == pygame.K_DOWN:
                main_player.speed_y = 0
            elif event.key == pygame.K_LEFT:
                main_player.speed_x = 0
            elif event.key == pygame.K_RIGHT:
                main_player.speed_x = 0
    if pygame.sprite.spritecollide(enemy, bullets, False):
        enemy.life = False
    if pygame.sprite.spritecollide(enemy1, bullets, False):
        enemy1.life = False
    if pygame.sprite.spritecollide(main_player, boosters, True, False):
        speed_const_x += 3
        speed_const_y -= 3
    if pygame.sprite.collide_rect(main_player, final):
        finish = True
        win.reset()
    if pygame.sprite.spritecollide(main_player, enemies, False):
        finish = True
        lose.reset()
    if pygame.sprite.spritecollide(main_player, enemies_y, False):
        finish = True
        lose.reset()
    if pygame.sprite.spritecollide(main_player, enemies_xy, False):
        finish = True
        lose.reset()
    if pygame.sprite.spritecollide(main_player, bullets2, False):
        finish = True
        lose.reset()

    if not finish:
        pygame.sprite.groupcollide(bullets, barriers, True, False)
        pygame.sprite.groupcollide(bullets2, barriers, True, False)
        pygame.sprite.groupcollide(bullets, enemies, True, True)
        pygame.sprite.groupcollide(bullets, enemies_y, True, True)
        pygame.sprite.groupcollide(bullets, enemies_xy, True, True)
        pygame.sprite.groupcollide(bullets, enemies3, True, True)
        window.fill((22, 43, 66))
        barriers.draw(window)
        enemies.draw(window)
        enemies_y.draw(window)
        enemies_xy.draw(window)
        enemies3.draw(window)
        bullets.draw(window)
        bullets2.draw(window)
        boosters.draw(window)
        final.reset()
        main_player.reset()
        main_player.update()
        enemies.update()
        enemies_y.update()
        enemies_xy.update()
        bullets.update()
        bullets2.update()

    if enemy.life == True:
        if enemy_fire == 0:
            enemy.fire()
            enemy_fire = 60
        else:
            enemy_fire -= 1
    if enemy1.life == True:
        if enemy_fire == 0:
            enemy.fire_left()
            enemy_fire = 60
        else:
            enemy_fire -= 1

    clock.tick(40)
    pygame.display.update()
