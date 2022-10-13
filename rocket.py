import sys
import pygame

from rocket_ship import Rocket

class RocketGame:
    
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("12-4 Rocket Challenge")
        
        self.bg_color = (230, 230, 230)
        self.screen_rect = self.screen.get_rect()
        
        self.rocket = Rocket(self)
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
            self.rocket.update()
            self._update_screen()
                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
    def _update_screen(self):                
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        
        pygame.display.flip()

            
if __name__ == '__main__':
    r = RocketGame()
    r.run_game()