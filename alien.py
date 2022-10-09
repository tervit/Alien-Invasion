import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self, ai_game):
		"""Інаціалізувати прибульця та задати його початкове розташування"""
		super().__init__()
		self.screen = ai_game.screen

		# Завантажити зображення прибульця та отримати його rect
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# Створювати кожного нового прибульця біля лівому верхньому куті екрану.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Зберегти точне горизонтальне положення прибульця
		self.x = float(self.rect.x)