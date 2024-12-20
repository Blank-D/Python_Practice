import pygame
from pygame.sprite import Sprite
from settings import Settings

class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()

        # 向右移动标志
        self.move_right = False

        # 向左移动标志
        self.move_left = False

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """根据移动标志调整飞船位置"""

        if self.move_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.move_left and self.rect.left >= 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        """让飞船在屏幕底部居中"""

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
