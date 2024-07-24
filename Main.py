import pygame

# start pygame
pygame.init()
# display
tela = pygame.display.set_mode((1280, 720))
# clock
tempo = pygame.time.Clock()
# char (whatever for now)
personagem = pygame.image.load('personagens/bigze.png').convert_alpha()
personagemrect = personagem.get_rect(center=(600, 300))
direcao_personagem = pygame.math.Vector2()
velocidade = 500
# arma
tiro = pygame.image.load('personagens/mic.png').convert_alpha()
tiros = []  # list to store bullets and their directions
velocidade_tiro = 700

# shooting variables
tempo_ultimo_tiro = pygame.time.get_ticks()  # time when last shot was fired
intervalo_tiro = 1000  # interval in milliseconds between shots (1 second)

# gameplay loop
jogo = True
while jogo:
    dt = tempo.tick(60) / 1000  # limit frame rate to 60 FPS
    # closing game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False

    # mover personagem
    keys = pygame.key.get_pressed()
    direcao_personagem.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    direcao_personagem.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    direcao_personagem = direcao_personagem.normalize() if direcao_personagem.length() > 0 else direcao_personagem
    personagemrect.center += direcao_personagem * velocidade * dt

    # atirar
    now = pygame.time.get_ticks()
    if now - tempo_ultimo_tiro > intervalo_tiro:
        mouse = pygame.mouse.get_pos()
        direcao_tiro = pygame.math.Vector2(mouse[0] - personagemrect.centerx, mouse[1] - personagemrect.centery)
        direcao_tiro = direcao_tiro.normalize() if direcao_tiro.length() > 0 else direcao_tiro
        tiros.append({'rect': tiro.get_rect(center=personagemrect.center), 'direction': direcao_tiro})  # add bullet rect and direction to list
        tempo_ultimo_tiro = now  # update time of last shot

    # move bullets
    for bullet in tiros:
        bullet['rect'].center += bullet['direction'] * velocidade_tiro * dt

    # color display
    tela.fill('aquamarine')

    # desenhar o personagem
    tela.blit(personagem, personagemrect)

    # draw bullets
    for bullet in tiros:
        tela.blit(tiro, bullet['rect'])

    # put on screen
    pygame.display.flip()

    # caption
    pygame.display.set_caption('really cool game')

pygame.quit()