from settings import *
from personagem import Player
from sprites import *
import math
import random
from random import randint , choice
from groups import Allsprites

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("ze")
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_images()

        #groups
        self.all_sprites = Allsprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


        # timer shoot
        self.can_shoot = True
        self.shoot_time = 0
        self.gun_cooldown = 100

        #timer enemy
        self.enemy_event = pygame.event.custom_type()
        pygame.time.set_timer(self.enemy_event, 300)
        self.spawn_positions = []
        
        
    

        # background
        self.bg = pygame.image.load('backgrounds/grass.jpg').convert()
        self.bg_width = self.bg.get_width()
        self.bg_height = self.bg.get_height()
        
        self.tiles_x = math.ceil(WINDOW_WIDTH / self.bg_width) + 1
        self.tiles_y = math.ceil(WINDOW_HEIGHT / self.bg_height) + 1
        
        self.player = Player((400,300), self.all_sprites, self.collision_sprites)
        self.gun = Gun(self.player, self.all_sprites)
        
    def load_images(self):
        self.bullet_surf = pygame.image.load('sprites/mic.png')
        

    def enemy_spawner(self):
        if random.choice([True, False]):
            self.enemy_x = 0
        else:
            self.enemy_x = self.player.rect.x * 2

        self.enemy_y = randint(0, WINDOW_HEIGHT) 

        return [self.enemy_x, self.enemy_y]      

    def input(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            pos = self.gun.rect.center + self.gun.player_direction * 100
            Bullet(self.bullet_surf, pos, self.gun.player_direction, (self.all_sprites, self.bullet_sprites))
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
            
    def timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.gun_cooldown:
                self.can_shoot = True

    def run(self):
        while self.running:
            #dts    
            dt = self.clock.tick() / 1000

            
            
            
            #event_loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.enemy_event:
                    enemy_pos = self.enemy_spawner()
                    Enemies(enemy_pos, (self.all_sprites,self.enemy_sprites), self.player, self.collision_sprites)
                        

           



            #update
            self.timer()
            self.input()
            self.all_sprites.update(dt)
        
            #draw
            offset_x = self.player.rect.centerx - WINDOW_WIDTH // 2
            offset_y = self.player.rect.centery - WINDOW_HEIGHT // 2

            for i in range(self.tiles_x):
                for j in range(self.tiles_y):
                    self.display_surface.blit(self.bg, (i * self.bg_width - offset_x % self.bg_width, j * self.bg_height - offset_y % self.bg_height))

            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()
            
        
        pygame.quit()

game = Game()
game.run()