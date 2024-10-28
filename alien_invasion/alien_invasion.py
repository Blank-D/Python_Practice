import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

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

        # 创建存储游戏统计信息的实例
        # 并创建记分牌
        # 创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        # 创建一个编组，存储所有有效的子弹：pygame.sprite.Group类似列表，主功能：绘制子弹以及更新每颗子弹的位置
        self.bullets = pygame.sprite.Group()

        # 创建外星人
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # 设置背景色(已在settings实现该功能)
        # self.bg_color = self.settings.bg_color


        # 创建Play按钮
        self.play_button = Button(self, 'Play')


    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 响应案件和鼠标事件
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # get_pos返回一个元组，包含玩家单机鼠标的x,y坐标
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """在玩家单机Play按钮时开始新游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # 修复缺陷，按钮不可见时，点该play位置也有效
        if button_clicked and not self.stats.game_active:
            # 重置游戏设置
            self.settings.initialize_dynamic_settings()
            # 重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群外星人并让飞船居中
            self._create_fleet()
            self.ship.center_ship()

            # 隐藏鼠标光标
            pygame.mouse.set_visible(False)



    def _check_keydown_events(self,event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            # 向左移动飞船
            self.ship.move_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
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
        # sprites返回一个列表
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 更新外星人的位置，将编组每个元素进行绘制，参数指定了要将编组中的元素绘制到哪个surface上
        self.aliens.draw(self.screen)

        # 显示得分
        self.sb.show_score()

        # 如果游戏中处于非活动状态，就绘制Play按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""

        if len(self.bullets) < self.settings.bullets_allowed:
            #创建新子弹并将其加入编组bullets中
            new_bullet = Bullet(self)
            # add方法，将子弹都存储在编组中，类似于append，专门为pygame编组编写
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""

        #更新子弹的位置
        self.bullets.update()

        # 删除消失的子弹,遍历编组的副本（因为python规定循环长度保持不变，所以不能从for循环遍历的列表或编组中删除元素）
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人碰撞"""
        # 删除发生碰撞的子弹和外星人
        # 检查是否有子弹击中了外星人,如果是，就删除相应的子弹和外星人
        # 原理：将一个编组中每个元素的rect同另一个编组中每个元素的rect进行比较，返回一个字典，其中包含了发生碰撞的子弹和外星人
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for aliens in collisions.values():
                # 单个子弹击中多个外星人，collisions返回一个列表*分数
                self.stats.score += self.settings.alien_points * len(aliens)
                # self.stats.score += self.settings.alien_points
                self.sb.prep_score()
                self.sb.check_high_score()

        # 判断外星人是否被击杀完
        if not self.aliens:
            # 删除现有的子弹并新建一群外星人,empty删除编组下的所有精灵
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # self.settings.bullet_speed += 1
            # self.settings.fleet_drop_speed += 5

            # 提高等级
            self.stats.level += 1
            self.sb.prep_level()


    def _create_fleet(self):
        """创建外星人群"""
        # 创建一个外星人并计算一行可容纳多少个外星人
        # 外星人的间距为外星人宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size     # size属性返回一个元组
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

        # 创建第一行外星人(教材)
        # for alien_number in range(number_alien_x):
        #     # 创建一个外星人并将其加入当前行
        #     self._create_alien(alien_number)

        # 按照中心点可以放多个(DIY)
        # px_alien_center_x = self.settings.screen_width // (number_alien_x + 1)
        # for alien_number in range(number_alien_x):
        #     alien = Alien(self)
        #     alien.rect.centerx = px_alien_center_x + px_alien_center_x * alien_number
        #     self.aliens.add(alien)

    def _create_alien(self, alien_number, row_number):
        """创建一个外星人并将其放在当前行"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """检查是否有外星人位于屏幕边缘
        更新外星人群中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船之间的碰撞,参数：一个精灵，一个编组，判断二者是否发生碰撞，无则返回None
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 检测外星人和屏幕底部发生碰撞
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取响应的措施"""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._changes_fleet_direction()
                break
    def _changes_fleet_direction(self):
        """将整群外星人下移，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """响应飞船被外星人撞到"""

        if self.stats.ships_left > 0:
            # 将ships_left减1
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人，并将飞船放到屏幕底端的中央
            self._create_fleet()
            self.ship.center_ship()

            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕底部"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被装到一样处理
                self._ship_hit()
                break

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
