import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ship):
	# 响应按键
	if event.key==pygame.K_RIGHT:
		# 向右移动飞船 
		ship.moving_right = True
	elif event.key==pygame.K_LEFT:
		#向左移动飞船
		ship.moving_left = True
	elif event.key==pygame.K_UP:
		#向上移动飞船
		ship.moving_up = True
	elif event.key==pygame.K_DOWN:
		#向下移动飞船
		ship.moving_down = True
	elif event.key == pygame.K_q:
		# 按q退出游戏
			sys.exit()
		
def check_keyup_events(event,ship):
	# 松开按键
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key==pygame.K_UP:
		ship.moving_up = False
	elif event.key==pygame.K_DOWN:
		ship.moving_down = False


def bullet_events(ai_settings,screen,ship,bullets):
	# 子弹事件
	new_bullet = Bullet(ai_settings,screen,ship)
	bullets.add(new_bullet)


def check_events(ai_settings,screen,ship,bullets):
	# 响应键鼠事件
	# bullet_events(ai_settings,screen,ship,bullets)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship)
			bullet_events(ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			bullet_events(ai_settings,screen,ship,bullets)
				

def update_screen(ai_settings,screen,ship,bullets):
	# 更新屏幕，切换到新屏幕

	# 每次都重新绘制屏幕
	screen.fill(ai_settings.bg_color)
	# 重绘子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
			
	ship.blitme()

	# 让最近绘制的屏幕可见
	pygame.display.flip()
	
def update_bullets(bullets):
	# 更新子弹位置，并删除已消失子弹
	# 删除已经消失的子弹释放内存
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))
