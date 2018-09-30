# -*- coding: GBK -*-
import pygame 

class Ship():
	
	def __init__(self,ai_settings,screen):
		# ��ʼ���ɴ��������ó�ʼλ
		self.screen = screen
		self.ai_settings = ai_settings
		
		# ���طɴ���ͼ���һ�ȡ����Ӿ���
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# ��ÿ�ҷɴ���������Ļ�ײ�����
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# �ڷɴ��������centerx�д���С��ֵ
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		#�ƶ���־
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
		
	def update(self):
		# �����ƶ���־�����ɴ�λ��
		# ���·ɴ���centerֵ�������޸�rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.centery -= self.ai_settings.ship_speed_factor
		# ����rect����	
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
	
	def blitme(self):
		# ��ָ���ط����Ʒɴ�
		self.screen.blit(self.image,self.rect)
		
	def center_ship(self):
		# �ɴ���λ
		self.centerx = self.screen_rect.centerx
		self.centery = self.screen_rect.bottom - 21
		# self.blitme()
