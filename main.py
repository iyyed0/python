import pygame
import time
import random 
pygame.font.init()
WIDTH, HEIGHT = 1000, 500
WIN =pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
FONT = pygame.font.SysFont("comicsans", 30)
BG=pygame.transform.scale(pygame.image.load("desert.jpg"),(WIDTH, HEIGHT))
PLAYER_WIDTH=60
PLAYER_HEIGHT=30
PLAYER_VEL=5
bomb_WIDTH = 40
bomb_HEIGHT = 20
bomb_image=pygame.transform.scale(pygame.image.load("bomb.png"),(bomb_WIDTH,bomb_HEIGHT))
player_image=pygame.transform.scale(pygame.image.load("superman.png"),(PLAYER_WIDTH,PLAYER_HEIGHT))
STAR_VEL = 3
def draw(player,elapsed_time,bombs):
    WIN.blit(BG,(0,0))
    time_text=FONT.render(f'Time:{round(elapsed_time)} s',1,"red")
    WIN.blit(time_text,(10,10))
    for bomb in bombs:
        WIN.blit(bomb_image,bomb)
    WIN.blit(player_image,player)
    pygame.display.update()
def main():
    run=True
    player=pygame.Rect(200,HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH, PLAYER_HEIGHT)
    clock=pygame.time.Clock()
    start_time=time.time()
    elapsed_time=0
    bomb_count=0
    bomb_add_increment=2000
    hit=False
    bomb_VEL=3
    bombs=[]
    while run:
        bomb_count+=clock.tick(80)
        elapsed_time= time.time() - start_time
        if bomb_count>bomb_add_increment:
            for _ in range(3) :
                bomb_y = random.randint(0, HEIGHT - bomb_HEIGHT)
                bomb=pygame.Rect(WIDTH,bomb_y,bomb_WIDTH,bomb_HEIGHT)
                bombs.append(bomb)
                bomb_y = random.randint(0, HEIGHT - bomb_HEIGHT)
                bomb_add_increment=max(200,bomb_add_increment-50)
                bomb_count=0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x>0:
            player.x-=PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x<(WIDTH-PLAYER_WIDTH):
            player.x+=PLAYER_VEL
        if keys[pygame.K_UP] and player.y>0:
            player.y-=PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y<(HEIGHT-PLAYER_HEIGHT):
            player.y+=PLAYER_VEL
        for bomb in bombs[:]:
            bomb.x-=bomb_VEL
            if bomb.x<0:
                bombs.remove(bomb)
            elif bomb.x- bomb_WIDTH>=player.x and bomb.colliderect(player):
                bombs.remove(bomb)
                hit=True
                break
        if hit:
            lost_text=FONT.render("you lost!",1,"red")
            WIN.blit(lost_text,(WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        draw(player,elapsed_time,bombs)
    pygame.quit()
if __name__=='__main__':
    main()
