from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join('personagens', 'bigze.png')).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox_rect = self.rect.inflate(-90, 0)
        #movement
        self.direction = pygame.math.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites
    
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d] - keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s] - keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        
    def move(self, dt):
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')
        self.rect.center = self.hitbox_rect.center

    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top
                    if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom                    

    def update(self, dt):
        self.input()
        self.move(dt)
             