import pygame, time
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

crossImg = pygame.image.load('cross.png')
crossImg = pygame.transform.scale(crossImg, (150, 150))

noughtImg = pygame.image.load('nought.png')
noughtImg = pygame.transform.scale(noughtImg, (150, 150))

font = pygame.font.SysFont(None, 92)

text = font.render('NOUGHTS WINS!', True, (0, 0, 0))
textRect = text.get_rect()
textRect.center = (300, 300)

text2 = font.render('CROSSES WINS!', True, (0, 0, 0))
textRect2 = text2.get_rect()
textRect2.center = (300, 300)

text3 = font.render('Nobody won...', True, (0, 0, 0))
textRect3 = text3.get_rect()
textRect3.center = (300, 300)



def noughtwin():
  pygame.display.flip()
  time.sleep(2)
  screen.fill((0, 255, 0))
  screen.blit(text, textRect)
  pygame.display.flip()
  time.sleep(2)
  game_loop()

def crosswin():
  pygame.display.flip()
  time.sleep(2)
  screen.fill((0, 255, 0))
  screen.blit(text2, textRect2)
  pygame.display.flip()
  time.sleep(2)
  game_loop()


def game_loop():

  player1 = True
  occupied1 = False
  occupied2 = False
  occupied3 = False
  occupied4 = False
  occupied5 = False
  occupied6 = False
  occupied7 = False
  occupied8 = False
  occupied9 = False
  nought1 = False
  cross1 = False
  nought2 = False
  cross2 = False  
  nought3 = False
  cross3 = False
  nought4 = False
  cross4 = False
  nought5 = False
  cross5 = False
  nought6 = False
  cross6 = False
  nought7 = False
  cross7 = False
  nought8 = False
  cross8 = False
  nought9 = False
  cross9 = False


  done = False
  while not done:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        exit()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        game_loop()
      if event.type == pygame.MOUSEBUTTONDOWN:

        if pygame.mouse.get_pos()[0] < 200 and pygame.mouse.get_pos()[1] < 200 and occupied1 == False:
          print("Top left")
          occupied1 = True
          player1 = not player1
          if noughts == True:
            nought1 = True
          elif noughts == False:
            cross1 = True
        if pygame.mouse.get_pos()[0] < 400 and pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[1] < 200 and occupied2 == False:
          print("Top middle")
          occupied2 = True
          player1 = not player1
          if noughts == True:
            nought2 = True
          elif noughts == False:
            cross2 = True
        if pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[1] < 200 and occupied3 == False:
          print("Top right")
          occupied3 = True
          player1 = not player1
          if noughts == True:
            nought3 = True
          elif noughts == False:
            cross3 = True

        if pygame.mouse.get_pos()[0] < 200 and pygame.mouse.get_pos()[1] < 400 and pygame.mouse.get_pos()[1] > 200 and occupied4 == False:
          print("Middle left")
          occupied4 = True
          player1 = not player1
          if noughts == True:
            nought4 = True
          elif noughts == False:
            cross4 = True
        if pygame.mouse.get_pos()[0] < 400 and pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[1] < 400 and pygame.mouse.get_pos()[1] > 200 and occupied5 == False:
          print("Middle middle")
          occupied5 = True
          player1 = not player1
          if noughts == True:
            nought5 = True
          elif noughts == False:
            cross5 = True
        if pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[1] < 400 and pygame.mouse.get_pos()[1] > 200 and occupied6 == False:
          print("Middle right")
          occupied6 = True
          player1 = not player1
          if noughts == True:
            nought6 = True
          elif noughts == False:
            cross6 = True

        if pygame.mouse.get_pos()[0] < 200 and pygame.mouse.get_pos()[1] > 400 and occupied7 == False:
          print("Bottom left")
          occupied7 = True
          player1 = not player1
          if noughts == True:
            nought7 = True
          elif noughts == False:
            cross7 = True
        if pygame.mouse.get_pos()[0] < 400 and pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[1] > 400 and occupied8 == False:
          print("Bottom middle")
          occupied8 = True
          player1 = not player1
          if noughts == True:
            nought8 = True
          elif noughts == False:
            cross8 = True
        if pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[1] > 400 and occupied9 == False:
          print("Bottom right")
          occupied9 = True
          player1 = not player1
          if noughts == True:
            nought9 = True
          elif noughts == False:
            cross9 = True

    
    
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(198, 0, 3, 600))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(398, 0, 3, 600))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 198, 600, 3))    
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 398, 600, 3))

    if player1 == True:
      noughts = True
    elif player1 == False:
      noughts = False




    if nought1:
      screen.blit(noughtImg, (25, 25))
    elif cross1:
      screen.blit(crossImg, (25, 25))

    if nought2:
      screen.blit(noughtImg, (225, 25))
    elif cross2:
      screen.blit(crossImg, (225, 25))

    if nought3:
      screen.blit(noughtImg, (425, 25))
    elif cross3:
      screen.blit(crossImg, (425, 25))

    if nought4:
      screen.blit(noughtImg, (25, 225))
    elif cross4:
      screen.blit(crossImg, (25, 225))

    if nought5:
      screen.blit(noughtImg, (225, 225))
    elif cross5:
      screen.blit(crossImg, (225, 225))

    if nought6:
      screen.blit(noughtImg, (425, 225))
    elif cross6:
      screen.blit(crossImg, (425, 225))

    if nought7:
      screen.blit(noughtImg, (25, 425))
    elif cross7:
      screen.blit(crossImg, (25, 425))

    if nought8:
      screen.blit(noughtImg, (225, 425))
    elif cross8:
      screen.blit(crossImg, (225, 425))

    if nought9:
      screen.blit(noughtImg, (425, 425))
    elif cross9:
      screen.blit(crossImg, (425, 425))



    if nought1 and nought2 and nought3:
      noughtwin()
    if nought4 and nought5 and nought6:
      noughtwin()
    if nought7 and nought8 and nought9:
      noughtwin()

    if nought1 and nought4 and nought7:
      noughtwin()
    if nought2 and nought5 and nought8:
      noughtwin()
    if nought3 and nought6 and nought9:
      noughtwin()

    if nought1 and nought5 and nought9:
      noughtwin()
    if nought3 and nought5 and nought7:
      noughtwin()

    
    if cross1 and cross2 and cross3:
      crosswin()
    if cross4 and cross5 and cross6:
      crosswin()
    if cross7 and cross8 and cross9:
      crosswin()

    if cross1 and cross4 and cross7:
      crosswin()
    if cross2 and cross5 and cross8:
      crosswin()
    if cross3 and cross6 and cross9:
      crosswin()
    
    if cross1 and cross5 and cross9:
      crosswin()
    if cross3 and cross5 and cross7:
      crosswin()
    
    elif occupied1 and occupied2 and occupied3 and occupied4 and occupied5 and occupied6 and occupied7 and occupied8 and occupied9:
      pygame.display.flip()
      time.sleep(2)
      screen.fill((255, 165, 0))
      screen.blit(text3, textRect3)
      pygame.display.flip()
      time.sleep(2)
      game_loop()
    

    pygame.display.flip()
    clock.tick(70)

game_loop()