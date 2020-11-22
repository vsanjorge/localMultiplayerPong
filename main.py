import pygame

pygame.init()

pygame.display.set_caption("WannabePong")

size = 800, 600
screen = pygame.display.set_mode(size)
width, height = size
speed = [1, 1]
bgc = 255, 255, 255
fontControls = pygame.font.SysFont("monospace", 16)
font = pygame.font.SysFont("monospace", 26)
fontCount = pygame.font.SysFont("monospace", 42)
pelota = pygame.image.load("pelota.png")
pelotaRect = pelota.get_rect()
palaRoja = pygame.image.load("palaRoja.png")
palaRojaRect = palaRoja.get_rect()
palaAzul = pygame.image.load("palaAzul.png")
palaAzulRect = palaAzul.get_rect()
divisor = pygame.image.load("divisor.png")
divisorRect = divisor.get_rect()
strikesRojo = 0
strikesAzul = 0
countdown = 10
run = True

divisorRect.move_ip(400, 0)
palaRojaRect.move_ip(1, 300)
palaAzulRect.move_ip(773, 300)

while countdown > 0:
  count = fontCount.render("{0}".format(countdown), 1, (0,0,0))
  redControls = fontControls.render("Moves with W and S keys", 1, (0,0,0))
  blueControls = fontControls.render("Moves with UP and DOWN arrows", 1, (0,0,0))
  screen.fill(bgc)
  screen.blit(redControls, (5, 50))
  screen.blit(blueControls, (505, 50))
  screen.blit(count, (388, 250))
  pygame.display.flip()
  pygame.time.wait(1000)
  countdown -= 1

while run:
  pygame.time.delay(2)
  pelotaRect = pelotaRect.move(speed)
  keys = pygame.key.get_pressed()
  strikesRojoDisplay = font.render("Strikes: {0}".format(strikesRojo), 1, (0,0,0))
  strikesAzulDisplay = font.render("Strikes: {0}".format(strikesAzul), 1, (0,0,0))
  winnerRojo = font.render("RED WINS!", 1, (0,0,0))
  winnerAzul = font.render("BLUE WINS!", 1, (0,0,0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  if keys[pygame.K_w] and palaRojaRect.top <= 0:
    palaRojaRect = palaRojaRect.move(0, 0)
  elif keys[pygame.K_w]:
    palaRojaRect = palaRojaRect.move(0, -1)
  if keys[pygame.K_s] and palaRojaRect.bottom >= height:
    palaRojaRect = palaRojaRect.move(0, 0)
  elif keys[pygame.K_s]:
    palaRojaRect = palaRojaRect.move(0, 1)
  if keys[pygame.K_UP] and palaAzulRect.top <= 0:
    palaAzulRect = palaAzulRect.move(0, 0)
  elif keys[pygame.K_UP]:
    palaAzulRect = palaAzulRect.move(0, -1)
  if keys[pygame.K_DOWN] and palaAzulRect.bottom >= height:
    palaAzulRect = palaAzulRect.move(0, 0)
  elif keys[pygame.K_DOWN]:
    palaAzulRect = palaAzulRect.move(0, 1)
  if palaRojaRect.colliderect(pelotaRect):
    speed[0] = -speed[0]
  if palaAzulRect.colliderect(pelotaRect):
    speed[0] = -speed[0]
  if pelotaRect.left <= 0 or pelotaRect.right >= width:
    speed[0] = -speed[0]
    if pelotaRect.left <= 0:
      strikesRojo += 1
    elif pelotaRect.right >= width:
      strikesAzul += 1
  if pelotaRect.top <= 0 or pelotaRect.bottom >= height:
    speed[1] = -speed[1]
  if strikesRojo == 5 or strikesAzul == 5:
    run = False
      
  screen.fill(bgc)
  screen.blit(divisor, divisorRect)
  screen.blit(pelota, pelotaRect)
  screen.blit(palaRoja, palaRojaRect)
  screen.blit(palaAzul, palaAzulRect)
  screen.blit(strikesRojoDisplay, (5, 10))
  screen.blit(strikesAzulDisplay, (633, 10))
  pygame.display.flip()

screen.fill(bgc)
if strikesRojo == 5:
  screen.blit(winnerAzul, (333, 250))
  pygame.display.flip()
elif strikesAzul == 5:
  screen.blit(winnerRojo, (333, 250))
  pygame.display.flip()
pygame.time.wait(5000)
pygame.QUIT()