import pygame

from dino_runner.utils.constants import FONT_STYLE
from dino_runner.utils.writer import Writer


class Score:
    def __init__(self):
        self.score = 0
        self.writer = Writer()
            
    def update(self, game):  
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 1
    def draw(self, screen):
        text, text_rect = self.writer.print(f"Score: {self.score}",FONT_STYLE, 24, 950,30)
        screen.blit(text, text_rect)
     
    def reset(self):
        self.score = 0