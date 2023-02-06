import pygame
import menu

menu = menu.Menu()
menu.run()
  
# pygame.init()
  
# color = (255,255,255)
# position = (0,0)
  
# # CREATING CANVAS
# canvas = pygame.display.set_mode((500,500))
  
# # TITLE OF CANVAS
# pygame.display.set_caption("Beer Run!")
  
# image = pygame.image.load("assets/beerrunsplash.jpg")
# exit = False
  
# while not exit:
#     canvas.fill(color)
#     canvas.blit(image, dest = position)
  
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit = True
#     rect_color = (255,0,0)
#     pygame.draw.rect(canvas, rect_color,
#                      pygame.Rect(30,30,60,60))
#     pygame.display.update()