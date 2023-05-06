from pygame import *

FPS = 60
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, p_image, width, height, x, y, speed):
        super().__init__()
        #self.image = transform.scale(image.load(player_image), (65, 65))
        self.image = transform.scale(image.load(p_image),(width , height))
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
 
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))  

window = display.set_mode((700,500))
display.set_caption('pingPong')

font.init()
font = font.SysFont('Arial', 40)

game = True
while game:
    window.blit('rock.jpg',(0,0))
    for el in event.get():
        if el.type == QUIT:
            game = False

    clock.tick(FPS)
    time.delay(5)
    display.update()

