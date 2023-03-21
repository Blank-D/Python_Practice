import pygame
import sys

from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()

        self.screen= pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))    #元组(游戏尺寸窗口)，返回为surface
        pygame.display.set_caption("Allen Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():    #返回列表，包含上一次被调用后发生的所有事件
                self._check_events()
                self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到更新屏幕"""
        #  每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)    # fill() 用于处理surface，接受一个参数
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()   # 每次绘制一个空屏幕，并擦去旧屏幕，显示新屏幕(不断更新屏幕)
if __name__ == '__main__':
    # 创建游戏实例并与运行游戏
    ai = AlienInvasion()
    ai.run_game()