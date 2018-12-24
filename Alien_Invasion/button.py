import pygame.font


class Button():
    def __init__(self,aliens_settings,screen,msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()

        self.width,self.height=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)

        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        self.msg=msg
        self.prep_msg()

    def prep_msg(self):
        self.msg_image=self.font.render(self.msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()#这里必须用个变量保存,以便保存设置好的属性.直接调用会获得默认属性.
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):

        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
