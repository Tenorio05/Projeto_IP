import pygame

pygame.init()

# Display
tela = pygame.display.set_mode((1280, 720))

# time
tempo = pygame.time.Clock()

# Char (whatever for now)
personagem = pygame.image.load('personagens/bigze.png').convert_alpha()
personagemrect = personagem.get_rect(center=(640, 360))  # Center of the screen
direcao_personagem = pygame.math.Vector2()
velocidade = 500

# Background provisional
bg = pygame.image.load('backgrounds/plains.png').convert()
bgrect = bg.get_rect()

# Arma
tiro = pygame.image.load('personagens/mic.png').convert_alpha()
tiros = []  # List to store bullets and their directions
velocidade_tiro = 700

# Shooting variables
tempo_ultimo_tiro = pygame.time.get_ticks()  # Time when last shot was fired
intervalo_tiro = 1000  # Interval in milliseconds between shots (1 second)

# Initial background offset
bg_offset_x = 0
bg_offset_y = 0

# Gameplay loop
jogo = True
while jogo:
    dt = tempo.tick(60) / 1000  
    
    # fechar jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False

    # movimento
    keys = pygame.key.get_pressed()
    direcao_personagem.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    direcao_personagem.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    direcao_personagem = direcao_personagem.normalize() if direcao_personagem.length() > 0 else direcao_personagem
    movimento = direcao_personagem * velocidade * dt
    
    # mover o background 
    bg_offset_x -= movimento.x
    bg_offset_y -= movimento.y

    # limitar o background
    bg_offset_x = max(min(bg_offset_x, 0), tela.get_width() - bg.get_width())
    bg_offset_y = max(min(bg_offset_y, 0), tela.get_height() - bg.get_height())

    # atirar
    now = pygame.time.get_ticks()
    if now - tempo_ultimo_tiro > intervalo_tiro:
        mouse = pygame.mouse.get_pos()
        direcao_tiro = pygame.math.Vector2(mouse[0] - personagemrect.centerx, mouse[1] - personagemrect.centery)
        direcao_tiro = direcao_tiro.normalize() if direcao_tiro.length() > 0 else direcao_tiro
        tiros.append({'rect': tiro.get_rect(center=personagemrect.center), 'direction': direcao_tiro})  # Add bullet rect and direction to list
        tempo_ultimo_tiro = now  # Update time of last shot

    # update do tiro
    for bullet in tiros:
        bullet['rect'].center += bullet['direction'] * velocidade_tiro * dt

    # desenhar bg
    tela.fill([255, 255, 255])
    tela.blit(bg, (bg_offset_x, bg_offset_y))

    # desenhar char
    tela.blit(personagem, personagemrect)

    # desenhar balas
    for bullet in tiros:
        tela.blit(tiro, bullet['rect'])

    # Update display
    pygame.display.flip()

    # titulo
    pygame.display.set_caption('nerissa ravencroft e ze vaqueiro')

pygame.quit()