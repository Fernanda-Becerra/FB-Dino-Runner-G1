import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus, CactusLarge


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game_speed, player, game):
        if not self.obstacles:
            obstacle_type = random.randint(0, 2)
            if obstacle_type == 0:
                self.obstacles.append(Cactus())
            else:
                self.obstacles.append(CactusLarge())
      
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)