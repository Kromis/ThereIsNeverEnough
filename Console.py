import os, sys
import pygame
import resources

#The Console class will display the "console" object on the screen 
#
class Console:
	def __init__(self, screen, messages):
		self.font = pygame.font.match_font('calibri')
		self.screen = screen
		self.console_img = resources.all_sprites['console.png']
		self.message_list = []
		self.console_pos = (638, 30)
		print(self.font.get_linesize())
		
		self.m1 = 'H'
		self.m2 = 'E'
		self.m3 = 'L'
		self.m4 = 'L'
		self.m5 = 'O'
		
		self.message_list.append(m1)
		self.message_list.append(m2)
		self.message_list.append(m3)
		self.message_list.append(m4)
		self.message_list.append(m5)
		
	
	def draw(self):
		screen.blit(self.console_img, self.console_pos)
		for m in message_list:
			self.console_output = pygame.font.Font.render(m.message, true, pygame.Color(255, 255, 255), 0)	
			screen.blit (self.console_output, (648, 40))
		
		#get_message grabs the next object in a message queue
	def get_message(self, incoming_message_queue):
		if len(incoming_message_queue) != 0:
			self.message = self.message_list.pop([0])
			
		if len(self.message_list) > 5:
			self.message_list.pop([0])
		
		self.message_list.append(self.message)
		
			
		
			
			
		
		
	
		
		
	
		
		