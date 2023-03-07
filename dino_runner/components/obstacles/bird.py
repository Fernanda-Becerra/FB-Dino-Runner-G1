from random import Random
import random
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_HEIGHT, SCREEN_WIDTH


class Bird(Obstacle):
    def __init__ (self):
        self.image = BIRD[0]
        self.type = "bird"
        self.step = 0
        self.bird_y = random.randint(200,(SCREEN_HEIGHT - 290))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacle):
        image = BIRD[self.step // 5]
        self.image = image
        self.rect.y = self.bird_y
        self.step += 1
        if self.step >= 10:
            self.step = 0
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacle.remove(self)
