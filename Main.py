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
        self.title = True
        self.dead = False
        self.pontos = 0
        
        #groups
        self.all_sprites = Allsprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.coin_sprites = pygame.sprite.Group()
        self.coraçao = pygame.sprite.Group()
        self.vida_sprites = pygame.sprite.Group()
        self.xp_sprites = pygame.sprite.Group()

        #placar moedas
        self.font_score = pygame.font.Font(join("fontes/PressStart2P.ttf"), 50)
        self.score = 0
        self.text_surf_score = self.font_score.render('X' + str(self.score), True, "yellow")
        self.text_rect_score = self.text_surf_score.get_frect(bottomright= (1090, 65))

        #placar xp
        self.font_lv = pygame.font.Font(join("fontes/Oxanium-Bold.ttf"), 20)
        self.text_surf_lv = self.font_lv.render('Lv. ' + str(1), True, "white")
        self.text_rect_lv = self.text_surf_lv.get_frect(center = (635, 280))

        # timer shoot
        self.can_shoot = True
        self.shoot_time = 0
        self.gun_cooldown = 500

        #timer enemy
        self.enemy_event = pygame.event.custom_type()
        self.spawn_positions = []

        # background
        self.bg = pygame.image.load('backgrounds/map.png').convert()
        self.bg = pygame.transform.scale(self.bg, (2000, 2000))
        self.bg_width = self.bg.get_width()
        self.bg_height = self.bg.get_height()
        
        self.tiles_x = math.ceil(WINDOW_WIDTH / self.bg_width) + 1
        self.tiles_y = math.ceil(WINDOW_HEIGHT / self.bg_height) + 1
        
        self.player = Player((400,300), self.all_sprites, self.collision_sprites, self.coin_sprites, self.update_score, self.xp_sprites, self.update_xp, self.enemy_sprites, self.display_surface, self.vida_sprites)
        pygame.time.set_timer(self.enemy_event, int(700 / self.player.level))
        self.gun = Gun(self.player, self.all_sprites)
        self.vida = Coraçao(self.coraçao)
        
    def load_images(self):
        self.bullet_surf = pygame.image.load('sprites/mic.png')

    def enemy_spawner(self):
        if random.choice([True, False]):
            self.enemy_x = self.player.rect.x // 2
        else:
            self.enemy_x = self.player.rect.x * 2

        if random.choice([True, False]):
            self.enemy_y = self.player.rect.y // 2
        else:
            self.enemy_y = self.player.rect.y * 2

        return [self.enemy_x, self.enemy_y]      

    def update_score(self):
        self.score += 1
        self.text_surf_score = self.font_score.render('X' + str(self.score), True, "yellow")

    def update_xp(self):
        self.player.xp += 1
        if self.player.xp == self.player.level * 25:
            self.player.level += 1
            self.player.xp = 0

        self.text_surf_lv = self.font_lv.render('Lv. ' + str(self.player.level), True, "white")

    def input(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            pos = self.gun.rect.center + self.gun.player_direction * 100
            Bullet(self.bullet_surf, pos, self.gun.player_direction, (self.all_sprites, self.bullet_sprites))
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.gun_cooldown / self.player.level:
                self.can_shoot = True

    def run(self):
        while self.running:
            #dts    
            dt = self.clock.tick() / 1000
            
            if self.title:
                self.dead = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                
                self.title_screen = pygame.image.load('backgrounds/1.png')
                self.title_screen = pygame.transform.scale(self.title_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
                self.display_surface.blit(self.title_screen, (0, 0))

                keys = pygame.key.get_pressed()

                if keys[pygame.K_RETURN]:
                    self.title = False
            
            else:
                if self.dead:
                    if self.pontos < self.score:
                        self.pontos += 1
                    
                    self.spawn_positions = []

                    for sprite in [self.coin_sprites, self.enemy_sprites, self.vida_sprites]:
                        for s in sprite:
                          s.kill()

                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                    
                    
                    score_font = pygame.font.Font(join("fontes/PressStart2P.ttf"), 50)
                    
                    score_text = score_font.render('Your Score: ' + str( self.pontos + ((self.player.level - 1) * 100)), True, 'yellow')
                    
                    
                    score_text_surface = score_text.get_frect()
                    dead_screen = pygame.image.load('backgrounds/2.png')
                    dead_screen = pygame.transform.scale(dead_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
                    self.display_surface.blit(dead_screen, (0,0))
                    self.display_surface.blit(score_text, (WINDOW_WIDTH/12, WINDOW_HEIGHT/2), score_text_surface)


                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_SPACE]:
                        self.dead = False
                        self.score = -1
                        self.player.vida = 4
                        self.pontos = 0
                        self.player.level = 1
                        self.player.xp = -1
                        self.update_score()
                        self.update_xp()

                    elif keys[pygame.K_BACKSPACE]:
                        self.title = True
                        self.dead = False
                        self.score = -1
                        self.player.vida = 4
                        self.pontos = 0
                        self.player.level = 1
                        self.player.xp = -1
                        self.update_score()
                        self.update_xp()

                else:
                    #event_loop
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                        if event.type == self.enemy_event:
                            enemy_pos = self.enemy_spawner()
                            
                            Enemies(enemy_pos, (self.all_sprites,self.enemy_sprites), self.player, self.collision_sprites, self.player.level)
                    
                    #gerar os coletáveis
                    for sprite in self.enemy_sprites:
                        if pygame.sprite.spritecollide(sprite, self.bullet_sprites, True):
                            drop = random.randint(1, 20)
                            if 18 >= drop >= 13:
                                self.coin = Coin((sprite.rect.centerx, sprite.rect.centery), (self.all_sprites, self.coin_sprites))
                            
                            elif drop >= 19:
                                self.item = Vida((sprite.rect.centerx, sprite.rect.centery), (self.all_sprites, self.vida_sprites))
                            
                            elif 12 >= drop >= 4:
                                self.xp = Xp((sprite.rect.centerx, sprite.rect.centery), (self.all_sprites, self.xp_sprites))

                            sprite.kill()

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
                    self.display_surface.blit(self.text_surf_score, self.text_rect_score)
                    coin = pygame.image.load('coin/2.png')
                    coin = pygame.transform.scale(coin, (70, 70))
                    self.display_surface.blit(coin, (925, 0))
                    self.display_surface.blit(self.text_surf_lv, self.text_rect_lv)
                    barra = int((self.player.xp *(1/(self.player.level * 25))) * 70)
                    pygame.draw.rect(self.display_surface, 'blue',((600, 290), (barra, 7 )))
                    pygame.draw.rect(self.display_surface, 'white',((600, 290), (70, 7 )), 2)

                    for i in range(self.player.vida):
                        self.vida.update(dt)
                        self.display_surface.blit(self.vida.image, (20 + i * 60, -1))

                    if self.player.vida <= 0:
                        self.dead = True
                    
            pygame.display.update()
            
            #print(self.player.xp)
            #print(self.player.level)
        pygame.quit()

game = Game()
game.run()