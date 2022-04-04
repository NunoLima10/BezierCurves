
import pygame
from  math import  floor

pygame.init()


class RadioButton:
    def __init__(self,position:tuple, color:tuple, radius:int, label:str) -> None:
        super().__init__()
        self.position = position
        self.color = color
        self.label = label
        self.radius = radius
        self.width = 1

        self.on_focus = False
        self.selected = True
        self.label_is_visibel =True

        self.font = "monospace"
        self.font_size = 25
        self.font_color = (255,255,255)

        self.center_circle_proportion = 1.9
        self.center_circle_color = (0,255,0)


    def draw_button(self, surface) -> None:
        if self.label_is_visibel: 
            self.draw_label(surface)

        radius = self.radius + 2 if self.on_focus  else self.radius 

        if self.selected: 
            pygame.draw.circle(surface, self.center_circle_color, self.position, radius / self.center_circle_proportion)

        pygame.draw.circle(surface, self.color, self.position, radius, self.width)
       
        

    def draw_label(self, surface) -> None:
        text_font = pygame.font.SysFont(self.font,self.font_size)
        text = text_font.render(self.label,1,self.font_color)
        text_rect = text.get_rect()
        text_rect.topleft = (self.position[0] + self.radius + 10, self.position[1] - self.font_size / 2)
        surface.blit(text,text_rect)

    def is_on_focus(self, position) -> bool:
        deltaX = (self.position[0] - position[0]) ** 2
        deltaY = (self.position[1] - position[1]) ** 2

        self.on_focus = self.radius > (deltaX + deltaY) ** 0.5 
        return self.on_focus

    def set_state(self,state) -> None:
        self.selected = state   



    
