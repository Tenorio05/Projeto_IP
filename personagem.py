from settings import *
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites, coin_sprites, update_score, xp_sprites, update_xp, enemy_sprites, display_surface, vida_sprites):
        super().__init__(groups)
        self.load_sprites()
        self.vida = 4
        self.state = "right"
        self.animation_index = 0
        self.enemy_sprites = enemy_sprites
        self.display_surface = display_surface
        self.vida_sprite = vida_sprites

        self.image = pygame.image.load(join("animation", "left", "0.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 80))
        self.rect = self.image.get_frect(center = (pos))
        self.hitbox_rect = self.rect.inflate(-40, -30)

        #movement
        self.direction = pygame.math.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites

        #pontuacoes
        self.coin_sprites = coin_sprites
        self.update_score = update_score
        self.xp_sprites = xp_sprites
        self.update_xp = update_xp
        self.hp = 50
        self.xp = 0
        self.level = 1
    
    def load_sprites(self):
        self.frames = {"left" : [], "right" : []}
        for state in self.frames.keys():
            for folder, subfolder, file in walk(join("animation", state)):
                if file:
                    for name in file:
                        sprite_atual = join(folder, name)
                        surf = pygame.image.load(sprite_atual).convert_alpha()
                        self.frames[state].append(surf)

    def animation(self, dt):
        if self.direction.x != 0 or self.direction.y != 0:
            if self.direction.x > 0:
                self.state = "right" 
            elif self.direction.x < 0:
                self.state = "left"
            self.animation_index += 10 * dt
            self.image = self.frames[self.state][int(self.animation_index) % len(self.frames[self.state])]
            self.image = pygame.transform.scale(self.image, (70, 80))
        else:
            self.image = self.frames[self.state][0 % len(self.frames[self.state])]
            self.image = pygame.transform.scale(self.image, (70, 80))

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

        for sprite in self.coin_sprites:
            if pygame.sprite.spritecollide(self, self.coin_sprites, True):
                self.update_score()  
        
        for sprite in self.xp_sprites:
            if pygame.sprite.spritecollide(self, self.xp_sprites, True):
                self.update_xp()
        
        for sprite in self.vida_sprite:
            if pygame.sprite.spritecollide(self, self.vida_sprite, True):
                self.vida +=1 

                if self.vida > 4:
                    self.vida = 4
                    for i in range(10):
                        self.update_score()
                    
        for sprite in self.enemy_sprites:
            if pygame.sprite.spritecollide(self, self.enemy_sprites, True):
                self.vida -= 1

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animation(dt)
             