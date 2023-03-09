from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE, SCREEN_WIDTH


class Hammer(PowerUp):
    POS_X = 80
    POS_Y = 320
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        self.rect = self.image.get_rect()
        self.rect.y = self.POS_Y
        self.rect.x = SCREEN_WIDTH
        super().__init__(HAMMER, HAMMER_TYPE)

    def set_pos(self, rect_new): #posicion inicial
        self.rect = rect_new
        return self
    
    def move_hammer(self, screen):
        self.rect.x += 25
        print(self.rect.x)
        screen.blit(self.image, self.rect)