import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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
				

def update_screen(ai_settings,screen,ship,aliens,bullets):
	# ������Ļ���л�������Ļ

	# ÿ�ζ����»�����Ļ
	screen.fill(ai_settings.bg_color)
	# �ػ��ӵ�
	for bullet in bullets.sprites():
		bullet.draw_bullet()
			
	ship.blitme()
	aliens.draw(screen)

	# ��������Ƶ���Ļ�ɼ�
	pygame.display.flip()
	
def update_bullets(ai_settings,screen,ship,aliens,bullets):
	# �����ӵ�λ�ã���ɾ������ʧ�ӵ�
	# ɾ���Ѿ���ʧ���ӵ��ͷ��ڴ�
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))
		# ����Ƿ����
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)
    
def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
	# ����Ƿ���У������У����ö�Ӧ���ӵ�����������ʧ
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    # if pygame.sprite.spritecollideany(ship,aliens):
        # bullets.empty()
	
    if len(aliens) == 0:
		# Ŀǰ��������ʧ�꣬���´�����������
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
	
def create_fleet(ai_settings,screen,ship,aliens):
	# ����������Ⱥ
	# ����һ�������ˣ�������һ�п������ɶ��ٸ�������
	# �����˼��Ϊ�����˿��
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,
					alien.rect.height)
	# ������һ��������
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
		# ����һ�������˲��ҽ�����뵱ǰ��		
			creat_alien(ai_settings,screen,aliens,alien_number,row_number)
	
def get_number_aliens_x(ai_settings,alien_width):
	# ����ÿ�п������ɶ��ٸ�������
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
	# ����һ�������˲��ҷ��ڵ�ǰ��
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)
	
def get_number_rows(ai_settings,ship_height,alien_height):
	# ������Ļ�������ɶ�����������
	available_space_y = (ai_settings.screen_height - (3 * alien_height)- ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
	# ����������Ⱥ�����е�������λ��
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	# �����ײ
	if pygame.sprite.spritecollideany(ship,aliens):
		# print("Ship hit!!!")
	    ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
	
def check_fleet_edges(ai_settings,aliens):
	# �������˵����Եʱ��ȡ��ʩ
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break
			
			
def change_fleet_direction(ai_settings,aliens):
	
	# �����������ƣ����ı����ǵķ���
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
	

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
	# ��Ӧײ��
	# ��ship_left��1
    if stats.ships_left > 0:
        stats.ships_left -= 1
		# ����ӵ����������б�
        aliens.empty()
        bullets.empty()
	
	    # ����һȺ�µ������ˣ����ҽ��ɴ����ڳ�ʼλ��
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
	
	    # ��ͣ
        sleep(0.5)
    else:
        stats.game_active = False

	
