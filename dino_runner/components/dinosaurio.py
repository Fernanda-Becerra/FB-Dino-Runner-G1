import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING_SHIELD, FONT_STYLE, HAMMER, HAMMER_TYPE, JUMPING, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING, DUCKING, RUNNING_HAMMER, RUNNING_SHIELD, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, DUCKING_HAMMER
from dino_runner.utils.writer import Writer


DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "ducking"
DINO_HAMMER = "hammer"

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}


class Dinosaur(Sprite):
    POSITION_X = 80
    POSITION_Y = 310
    JUMP_VELOCITY = 8.5
    POSITION_DUCK = 340
    
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.hammer_img = None
        #en q momento deberia acabar el power up
        self.power_up_time_up = 0
        self.update_image(RUN_IMG[self.type][0])
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        self.step = 0
        self.writer = Writer()
        self.hammer_power  = False
   
    def update(self, user_input):
      if self.action == DINO_RUNNING:
         self.run()
      elif self.action == DINO_JUMPING:
         self.jump()
      elif self.action == DINO_DUCKING:
         self.duck()
      elif self.action == DINO_HAMMER:
         self.throw_hammer()
      
      if self.action != DINO_JUMPING:
        if user_input[pygame.K_UP]:
          self.action = DINO_JUMPING
        elif user_input[pygame.K_DOWN]: # Aqui el dinosaurio le ordenamos que se agache
          self.action = DINO_DUCKING
        elif user_input[pygame.K_RIGHT]:
           self.action = DINO_HAMMER
           self.hammer_power = True
        else:
           self.action = DINO_RUNNING

        if self.step >= 10:
            self.step = 0

    def jump(self):
        pos_y = self.rect.y - self.jump_velocity * 4
        self.update_image(JUMP_IMG[self.type], pos_y=pos_y)
        self.jump_velocity -= 0.8
    
        if self.jump_velocity < -self.JUMP_VELOCITY:
           self.jump_velocity = self.JUMP_VELOCITY
           self.action = DINO_RUNNING
           self.rect.y = self.POSITION_Y
    
    def update_image(self, image: pygame.Surface, pos_x=None, pos_y=None):
      self.image = image 
      self.rect = self.image.get_rect()
      self.rect.x = pos_x or self.POSITION_X
      self.rect.y = pos_y or self.POSITION_Y
       
    def duck(self):
      self.update_image(DUCK_IMG[self.type][self.step // 5], pos_y=self.POSITION_DUCK) 
      self.step += 1
    
    def throw_hammer(self):
      self.type = DEFAULT_TYPE
      self.image = RUN_IMG[self.type][0]
    
    def run(self):
      self.update_image(RUN_IMG[self.type][self.step // 5]) 
      self.step += 1
    
    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
       
    def on_pick_power_up(self,power_up):
       self.type = power_up.type
       self.power_up_time_up = power_up.start_time + (power_up.duration *1000)
    
    def check_power_up(self, screen):
      if self.type == SHIELD_TYPE:
        time_to_show = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
        if time_to_show >= 0: 
          text, text_rect = self.writer.print(f"{self.type.capitalize()} enabled for {time_to_show} seconds.", FONT_STYLE, 16, SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) - 250)
          screen.blit(text, text_rect)
        else:
          self.type = DEFAULT_TYPE
          self.power_up_time_up = 0
    