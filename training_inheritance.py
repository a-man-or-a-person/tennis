from pygame import *
from random import randint




 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed,size_x,size_y):
        super().__init__()
        self.image =transform.scale(image.load(player_image), (70,100))
        self.speed =player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    



font.init()
window = display.set_mode ((700,600))
display.set_caption ("Mad Max")
back= transform.scale(image.load("K.jpg"),(700,600))

               

        





class Player(GameSprite):
    def control(self):
        keypress = key.get_pressed()
        if keypress[K_w]:
            self.rect.y = self.rect.y - self.speed


        if keypress[K_s]:
            self.rect.y = self.rect.y + self.speed




class Player1(GameSprite):
    def control(self):
        keypress = key.get_pressed()
        if keypress[K_UP]:
            self.rect.y = self.rect.y - self.speed


        if keypress[K_DOWN]:
            self.rect.y = self.rect.y + self.speed


        

ufo = GameSprite ("ufo.png",310,250,5,60,30)
kek1 =Player ("300px-Plank.png",0,500,5,60,50)
kek2 =Player1 ("300px-Plank.png",600,400,5,60,100)
ball = GameSprite("17-removebg-preview.png",100,200,2,20,30)

font.init()
font = font.Font(None,35)
lose1 = font.render("Numder 1 lose",True,(180,0,0))
lose2 = font.render("Number 2 lose",True,(180,0,0))


speed_x = 3
speed_y = 3







clock = time.Clock()
FPS = 60                                                             


finish = False
game = True
while game:
    kpe = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game=False
        
        
    if finish != True :
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(back,(0,0))
        kek1.reset()
        kek1.control()
        kek2.reset()
        kek2.control()
        ball.reset()
        

        
        ufo.reset()


        if sprite.collide_rect(kek1,ball) or sprite.collide_rect(kek2,ball):
            speed_x *= -1
            speed_y *= 1
        
    if ball.rect.x > 700 :
        lose1 = font.render("Numder 1 lose",True,(180,0,0))
        window.blit(lose1,(270,300))
    if ball.rect.x < 0 :
        lose2 = font.render("Number 2 lose",True,(180,0,0))  
        window.blit(lose2,(270,300))
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1    

        clock.tick(FPS)


        
        

            
        





        
    
    display.update()
