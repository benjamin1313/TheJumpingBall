import pygame, sys
from pygame.locals import *

pygame.init()

white = (255,255,255) 
black = (0,0,0)
red = (255,0,0)
green =(0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
brown = (112,34,0)


screen = pygame.display.set_mode((640,360),0,32)
pygame.display.set_caption("the jumping ball! v0.1.2")

font = pygame.font.Font(None,30)

title = pygame.image.load("TJB/start.png")
gameover = pygame.image.load("TJB/dead.png")

FPS = 30

fpstime = pygame.time.Clock()

cx = 75
cy = 291
log = 0
logx = 650
logy = 320


move = "stop"
inJumpUp = False
inJumpDown = False

status = "start"


while True:

  
  if status == "start": #the start screen for the game
    screen.fill(blue)
  
    pygame.draw.line(screen,green,(0,340),(640,340),50)
    pygame.draw.circle(screen,yellow,(580,50),40)
    screen.blit(title,(0,0))
    
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_RETURN:
          status = "runs"
          
      elif event.type == QUIT:
        pygame.quit()
        sys.exit

    pygame.display.update()
    fpstime.tick(FPS)

  elif status == "runs": # the running game
    screen.fill(blue)
    
    if logx == -25:
      logx = 650
    logx -= 5
    pygame.draw.line(screen,brown,(logx,logy-40),(logx,logy),40)

    pygame.draw.line(screen,green,(0,340),(640,340),50)
    pygame.draw.circle(screen,yellow,(580,50),40)
      
    if move == "right":
      cx += 5
      if cx > 640:
        move = "stop"
    elif move == "left":
      cx -= 5
      if cx < 0:
        move = "stop"
        
    if inJumpUp == True:
      cy -= 5
      if cy < 240:
        inJumpUp = False
        inJumpDown = True
    elif inJumpDown == True:
      cy += 5
      if cy == 291:
        inJumpDown = False
        
    if cx+12 > logx-20 and cx-12 < logx+25 and cy+12 > logy-25:
      status = "dead"
    
    pygame.draw.circle(screen,red,(cx,cy),25)
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_LEFT:
          move = "left"
        elif event.key == K_RIGHT:
          move = "right"
        elif event.key == K_UP:
          if inJumpDown == False:
            inJumpUp = True
      elif event.type == KEYUP:
        if event.key == K_LEFT:
          move = "stop"
        elif event.key == K_RIGHT:
          move = "stop"
      
      elif event.type == QUIT:
        pygame.quit()
        sys.exit

  if status == "dead": #when you die
    screen.fill(blue)

    pygame.draw.line(screen,brown,(logx,logy-40),(logx,logy),40)
    
    pygame.draw.line(screen,green,(0,340),(640,340),50)
    pygame.draw.circle(screen,yellow,(580,50),40)
    pygame.draw.circle(screen,red,(cx,cy),25)
    screen.blit(gameover,(0,0))
    
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_RETURN:
          cx = 75
          cy = 291
          logx = 650
          move = "stop"
          inJumpUp = False
          inJumpDown = False
          status = "runs"
        elif event.key == K_ESCAPE:
          pygame.quit()
          sys.exit
      elif event.type == QUIT:
        pygame.quit()
        sys.exit
      
  pygame.display.update()
  fpstime.tick(FPS)
