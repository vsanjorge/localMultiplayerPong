import pygame

pygame.init()

pygame.display.set_caption("WannabePong")

size = 800, 600
screen = pygame.display.set_mode(size)
width, height = size
speed = [1, 1]
bgc = 255, 255, 255
font = pygame.font.Sysfont("monospace", 26)
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
keys = pygame.key.get_pressed()

divisorRect.move_ip(400, 300)
palaRojaRect.move_ip(1, 300)
palaAzulRect.move_ip(799, 300)

while True:
  pygame.time.delay(1)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      False
  if keys[pygame.K_W] and palaRojaRect.top <= 0:
    palaRojaRect = palaRojaRect.move(0, 0)
  elif keys[pygame.K_W]:
    palaRojaRect = palaRojaRect.move(0, -1)
  if keys[pygame.K_S] and palaRojaRect.bottom >= height:
    palaRojaRect = palaRojaRect.move(0, 0)
  elif keys[pygame.K_S]:
    palaRojaRect = palaRojaRect.move(0, 1)
  if palaRojaRect.colliderect(pelotaRect)