import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game_speed, player, on_death):
        if not self.obstacles:
            obstacle_type = random.randint(0, 1)
            if obstacle_type == 0:
                self.obstacles.append(Cactus())
            else:
                self.obstacles.append(Bird())
                
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.rect.colliderect(obstacle.rect):
                on_death()
     
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    def reset(self):
        self.obstacles = []