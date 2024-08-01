from settings import *
from math import atan2, degrees

class Colisao(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = pygame.Surface(surf)
        self.image.fill('blue')
        self.rect = self.image.get_rect(center = pos)

class Gun(pygame.sprite.Sprite):


    def __init__(self, player, groups):
        #player part
        self.player = player
        self.distance = 180
        self.player_direction = pygame.Vector2(0, 1)

        #sprite part
        super().__init__(groups)
        self.gun_surface = pygame.image.load('sprites/arma.png')
        self.image = self.gun_surface
        self.rect = self.image.get_rect(center = self.player.rect.center + self.player_direction * self.distance)

    def direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.player_direction = (mouse_pos - player_pos).normalize()
        
    
    def rotation(self):
        angle = degrees(atan2(self.player_direction.x, self.player_direction.y)) - 90
        if self.player_direction.x > 0:
            self.image = pygame.transform.rotozoom(self.gun_surface, angle, 1)
        else:
            self.image = pygame.transform.rotozoom(self.gun_surface, abs(angle), 1)
            self.image = pygame.transform.flip(self.image, False, True)


    def update(self, _):
        self.direction()
        self.rotation()
        self.rect.center = self.player.rect.center + self.player_direction * self.distance     

class Bullet(pygame.sprite.Sprite):
    def __init__(self, surf, pos, direction, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(center = pos)
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 1000 

        self.direction = direction
        self.speed = 1200


    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt

        if pygame.time.get_ticks() - self.spawn_time >= self.lifetime:
            self.kill()    

class Enemies(pygame.sprite.Sprite):
    def __init__(self, pos, groups, player, collision_sprites):
        super().__init__(groups)
        self.player = player

        # image
        self.image = pygame.image.load('sprites/terrorist.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-20, -40)
        self.collision_sprites = collision_sprites
        self.direction = pygame.Vector2()
        self.speed = 100

    def update(self, dt):
    # Move towards player
        self.direction = pygame.Vector2(self.player.rect.center) - pygame.Vector2(self.rect.center)
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * self.speed * dt
    
    