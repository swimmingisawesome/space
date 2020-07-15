import pygame
from Ship import *
pygame.init()

screen_info = pygame.display.Info()
print(screen_info)

w = pygame.display.set_mode((800, 600))
c = pygame.time.Clock()
color = (30, 0, 30)

NumLevels = 4
Level = 1
AsteroidCount = 3
Player = Ship()


def main():
  while Level <= NumLevels:
    c.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key== pygame.K_RIGHT:
          Player.speed[0] = 10
    Player.update()
    w.fill(color)
    w.blit(Player.image, Player.rect)
    pygame.display.flip()

if __name__=='__main__':
  main() 




