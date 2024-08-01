from settings import *

class Allsprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offfset = pygame.Vector2()

    def draw(self, target_pos):
        self.offfset.x = -(target_pos[0] - WINDOW_WIDTH / 2)
        self.offfset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)
        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offfset)
