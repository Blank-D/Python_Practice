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

        # 开启全屏模式
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

        # 设置背景色(已在settings实现该功能)
        # self.bg_color = self.settings.bg_color


    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 响应案件和鼠标事件
            self._check_events()
            self.ship.update()
            # 每次循环时都重绘屏幕
            self._update_screen()
            # 让最近绘制的屏幕可见
            pygame.display.flip()

    def _check_events(self):
        """响应案件和鼠标事件"""
        for event in pygame.event.get():
            # 点击窗口的关闭按钮，触发QUIT事件，调用sys.exit()退出
            if event.type == pygame.QUIT:
                sys.exit()
            # 用户按键都将在pygame注册一个事件，通过pygame.event.get()获取，每次案件都被注册为一个KEYDOWN事件
            elif event.type == pygame.KEYDOWN: #768
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP: #769
                self._check_keyup_events(event)


    def _check_keydown_events(self,event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            # 向左移动飞船
            self.ship.move_left = True
        # 触发按键Q，进行退出游戏
        elif event.key == pygame.K_q: # 113
            sys.exit()

    def _check_keyup_events(self,event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False


    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
