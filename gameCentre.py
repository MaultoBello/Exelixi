import sys
import pygame
from settings import Settings

class GameCentre:
	""" Central class to coordinate game components """

	def __init__(self):

		self.settings = Settings()
		self.screen = pygame.display.set_mode(self.settings.screen_dimensions)

	def _update_screen():
		pygame.display.flip()

	def runGame(self):
		while True:
			self._update_screen()

if __name__ == "__main__":
	gameCentre = GameCentre()