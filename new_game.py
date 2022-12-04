import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("First Game")


#Drawing and moving the character 

x = 50 
y = 50 
width = 40 
height =60 
vel =5 

#All pygame have main loop 
run = True 

while run: 
    pygame.time.delay(100)
    
    #time_stamp: tech with tim pygame video 1, 06:16
    for event in pygame.event.get():
        #I think the without this it would close wihtout hitting x
          if event.type == pygame.QUIT:
              run = False
              
pygame.quit()
              
