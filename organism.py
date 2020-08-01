import pygame
from pygame.sprite import Sprite
import Settings()

class Organism(Sprite):

	def __init__(self, game_center, speed = 1, sight = 20):

		self.settings = settings()
		self.game_center = game_center
		self.screen = self.game_center.screen
		self.screen_rect = self. self.game_center.screen.get_rect()

		self.speed = speed
		self.sight = sight

		self.color = (200, 100, 50)

		self.rect = pygame.Rect(0, 0, 50, 50)

		self.rect.centerx = self.game_center.scren_rect.centerx
		self.rect.centery = self.game_center.scren_rect.centery

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		

	def draw(self):
		pygame.draw.rect(self.screen, self.color, self.rect)