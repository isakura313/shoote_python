import pygame, sys, random

Display = pygame.display.set_mode((640, 400)) #размер от 640 до 400
pygame.display.set_caption("SNIPER ELITE 3000")

target = pygame.image.load("cherep.jpg")
targetPosition = target.get_rect()
targetPosition.bottom = random.randint(32, 368)
targetPosition.left = random.randint(0, 592)

pygame.mixer.init()
tracks = ['music/dance.mp3', 'music/song.mp3', 'music/tiger.ogg']
pygame.mixer.music.load(random.choice(tracks))
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

while True:
    pygame.mouse.set_visible(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                shot = pygame.Rect(x, y, 1, 1)
                if shot.colliderect(targetPosition):
                    targetPosition.bottom = random.randint(32, 368)
                    targetPosition.left = random.randint(0, 592)
                shotSound = pygame.mixer.Sound("weapons/laser1.wav")
                shotSound.play()
    Display.fill((0,0,0))
    Display.blit(target, targetPosition)
    pygame.draw.line(Display, (255, 255, 255), (0, y), (640, y))
    pygame.draw.line(Display, (255, 255, 255), (x, 0), (x, 400))
    pygame.display.update()



