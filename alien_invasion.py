from settings import Settings
from ship import Ship
from pygame.sprite import Group
import pygame
import game_functions as gf


def run_game():
    # 初始化游戏并且创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    
    # 创建子弹编组
    bullets = Group()
	
	# 开始游戏的主循环
    while True:
        # 监视键鼠事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        # 更新屏幕
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets)


run_game()
