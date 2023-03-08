import pygame

class Writer:
    def print(self, message, font_style, font_size, width, height):
        font = pygame.font.Font(font_style, font_size)
        text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width, height)
        return text, text_rect