import pygame

class Rocket:
    
    def __init__(self, r_game):
        self.screen = r_game.screen
        self.screen_rect = r_game.screen.get_rect()
        
        self.image = pygame.image.load('images/rocket.bmp')
        self.image = pygame.transform.scale(self.image, (50, 100)) 
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        
        # For sideways shooter
        self.rect.x = 0
        self.rect.y = 400                 # move to location
        
        # self.rect.center = self.screen_rect.center
        
        # Movement Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
            
    def blitme(self):
        self.screen.blit(self.image, self.rect)