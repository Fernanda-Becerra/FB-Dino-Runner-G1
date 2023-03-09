import pygame
from dino_runner.components.dinosaurio import Dinosaur
from dino_runner.components.obstacles.obstacles_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score

from dino_runner.utils.constants import BG, DINO_START, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS
from dino_runner.utils.writer import Writer


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.excecuting = False
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager= ObstacleManager()
        self.score = Score()
        self.writer = Writer()
        self.death_count = 0
        # contador de muertes almacenado
        # Aqui guardo el valor de contador de muertes para mostrar
        self.death_count_stored = 0
        self.power_up_manager = PowerUpManager()

    def run(self):
        self.excecuting = True
        while self.excecuting:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def start_game(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset()
        self.power_up_manager.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.score.update(self)
        self.power_up_manager.update(self.game_speed, self.score.score, self.player)
        self.player.check_power_up(self.screen)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)     
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.player.check_power_up(self.screen)
        pygame.display.update()
        pygame.display.flip()
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
   
    def on_death(self):
        is_invincible = self.player.type == SHIELD_TYPE
        if not is_invincible:
            self.playing = False
            self.death_count =+ 1
        # Aqui voy actualizando el contador de muertes para mostrar
            self.death_count_stored += 1

    def show_menu(self):
         self.screen.fill((255, 255, 255))
        
         half_screen_width = SCREEN_WIDTH // 2
         half_screen_height = SCREEN_HEIGHT // 2

         if not self.death_count:
            text, text_rect = self.writer.print("Welcome, press any key to start...!", FONT_STYLE, 32, half_screen_width,half_screen_height)
            self.screen.blit(text, text_rect)
        
         else:
            print("entra o no")
            message_title = "You Loose!, press any key to continue...!"
            message_score = f"Score = {self.score.score}"
            message_death = f"Death Count = {self.death_count_stored}"
            font_size = 32

            result_title = self.writer.print(message_title, FONT_STYLE, font_size, half_screen_width, half_screen_height)
            self.screen.blit(result_title[0], result_title[1])

            result_score= self.writer.print(message_score, FONT_STYLE, font_size, half_screen_width, half_screen_height + 50)
            self.screen.blit(result_score[0], result_score[1])

            result_death= self.writer.print(message_death, FONT_STYLE, font_size, half_screen_width, half_screen_height + 100)
            self.screen.blit(result_death[0], result_death[1])


         self.screen.blit(DINO_START,(half_screen_width - 40, half_screen_height -140))
         pygame.display.flip()

         self.handle_menu_events()

    def handle_menu_events(self):
        # print("ENTRO AL FUCKING handle_menu_events function")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("ENTRO  AL QUIT JODER!!")
                self.playing = False
                self.executing = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                self.start_game()
    
