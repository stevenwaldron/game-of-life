import pygame
vec = pygame.math.Vector2

class Button: 
    def __init__(self,surface,x,y,width,height,state='',id='',function=None,color=(255,255,255),hover_color=(255,255,255),border=True,border_width=2,border_color=(0,0,0),text=None,bg_color=(5,5,5),text_size=20,font_name=None,bold_text=True,text_color=(10,10,10)):
        self.x = x 
        self.y = y
        self.pos = vec(x,y)
        self.width = width
        self.height = height
        self.surface = surface
        self.image = pygame.Surface((width,height))
        self.border = border
        self.border_width = border_width
        self.border_color = border_color
        self.color = color
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.hover = False
        self.state = state
        self.id = id
        self.function = function
        self.text = text
        self.font = pygame.font.SysFont('arial',20)
        self.text_size = text_size
        self.font_name = font_name
        self.bold_text = bold_text
        self.text_color = text_color
        

    def update(self,pos):
        if self.mouse_hovering(pos):
            self.hover = True
        else:
            self.hover = True

            
        # if self.x + self.width > cursor[0] > self.x and self.y+self.height > cursor[1] > self.y:
        #     self.hover = True
        # else:
        #     self.hover = False


    def draw(self):
        if self.border:
            self.image.fill(self.border_color)
            if self.hover:
                pygame.draw.rect(self.image,self.hover_color,(self.border_width,self.border_width,self.width-(self.border_width*2),self.height-(self.border_width*2)))
            else:
                pygame.draw.rect(self.image,self.color,(self.border_width,self.border_width,self.width-(self.border_width*2),self.height-(self.border_width*2)))
        else:
            self.image.fill(self.color)
        if len(self.text) > 0 or int(self.text) <= 0:
            self.show_text()
        self.surface.blit(self.image,self.pos)
        

            


    def click(self):
        if self.function != None and self.hover:
            self.function()
        else:
            pass

    def show_text(self):
        font = pygame.font.SysFont(self.font_name, self.text_size,bold=self.bold_text)
        text = font.render(self.text,False,self.text_color)
        size = text.get_size()
        x,y = self.width//2-(size[0]//2),self.height//2-(size[1]//2)
        pos = vec(x,y)
        self.image.blit(text,pos)

    def mouse_hovering(self,pos):
        if pos[0] > self.pos[0] and pos[0] < self.pos[0]+self.width:
            if pos[1] > self.pos[1] and pos[1] < self.pos[1]+self.height:
                return True
        else:
            return False
