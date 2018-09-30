# -*- coding: GBK -*-
import pygame 

class Ship():
	
	def __init__(self,ai_settings,screen):
		# 初始化飞船并且设置初始位
		self.screen = screen
		self.ai_settings = ai_settings
		
		# 加载飞船的图像并且获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# 将每艘飞船都置于屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# 在飞船的输出型centerx中储存小数值
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		#移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
		
	def update(self):
		# 根据移动标志调整飞船位置
		# 更新飞船的center值，而非修改rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.centery -= self.ai_settings.ship_speed_factor
		# 更新rect对象	
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
	
	def blitme(self):
		# 在指定地方绘制飞船
		self.screen.blit(self.image,self.rect)
		
	def center_ship(self):
		# 飞船归位
		self.centerx = self.screen_rect.centerx
		self.centery = self.screen_rect.bottom - 21
		# self.blitme()
