from pygame import * 

FPS = 60
win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("Shooter")
clock = time.Clock()

back = (200,255,255)
window.fill(back)


class GameSprite(sprite.Sprite):

    def __init__(self, x, y, width, height, speed):
        super().__init__()
        self.x = x  # x-coordinate of the top-left corner
        self.y = y  # y-coordinate of the top-left corner
        self.width = width  # Width of the paddle
        self.height = height  # Height of the paddle
        self.speed = speed  # Speed at which the paddle moves

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed 
game =True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 

    display.update()
    clock.tick(FPS)