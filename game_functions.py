import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ship):
	# ��Ӧ����
	if event.key==pygame.K_RIGHT:
		# �����ƶ��ɴ� 
		ship.moving_right = True
	elif event.key==pygame.K_LEFT:
		#�����ƶ��ɴ�
		ship.moving_left = True
	elif event.key==pygame.K_UP:
		#�����ƶ��ɴ�
		ship.moving_up = True
	elif event.key==pygame.K_DOWN:
		#�����ƶ��ɴ�
		ship.moving_down = True
	elif event.key == pygame.K_q:
		# ��q�˳���Ϸ
			sys.exit()
		
def check_keyup_events(event,ship):
	# �ɿ�����
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key==pygame.K_UP:
		ship.moving_up = False
	elif event.key==pygame.K_DOWN:
		ship.moving_down = False


def bullet_events(ai_settings,screen,ship,bullets):
	# �ӵ��¼�
	new_bullet = Bullet(ai_settings,screen,ship)
	bullets.add(new_bullet)


def check_events(ai_settings,screen,ship,bullets):
	# ��Ӧ�����¼�
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
	# ������Ļ���л�������Ļ

	# ÿ�ζ����»�����Ļ
	screen.fill(ai_settings.bg_color)
	# �ػ��ӵ�
	for bullet in bullets.sprites():
		bullet.draw_bullet()
			
	ship.blitme()

	# ��������Ƶ���Ļ�ɼ�
	pygame.display.flip()
	
def update_bullets(bullets):
	# �����ӵ�λ�ã���ɾ������ʧ�ӵ�
	# ɾ���Ѿ���ʧ���ӵ��ͷ��ڴ�
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))
