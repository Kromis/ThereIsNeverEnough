import os, sys
import pygame
import resources

#The Console class will display the "console" object on the screen 
#
class Console:

	def __init__(self, screen):
		self.font = pygame.font.Font(pygame.font.match_font('calibri'), 30)
		self.screen = screen
		self.console_img = resources.all_sprites['console.png']
		self.message_list = []
		self.message_list_max_size = 9
		self.console_pos = (628, 30)
		self.time = '[' + '{:02d}:{:02d}'.format(resources.time.hour, resources.time.minute) + '] '
		#Attach timestamp BEFORE appending
		self.message_list.append(self.time + '1 Incoming new message')
		self.message_list.append('2 Incoming new message')
		self.message_list.append('3 Incoming new message')
		self.message_list.append('4 Incoming new message')
		self.message_list.append('5 Incoming new message')
		self.message_list.append('6 Incoming new message')
		self.message_list.append('7 Incoming new message')
		self.message_list.append('8 Incoming new message')
		self.message_list.append('9 Incoming new message')
		self.message_list.append('9 Incoming new message')
		self.message_list.append('9 Incoming new message')
		self.message_list.append('9 Incoming new message')
		
	def draw(self):
		#self.timestamp = '[' + '{:02d}:{:02d}'.format(resources.game_manager.time.hour, resources.game_manager.time.minute) + '] '
		self.screen.blit(self.console_img, self.console_pos)
		#self.get_message()
		for m in range(len(self.message_list)):
			self.console_output = self.font.render(self.message_list[m], True, pygame.Color(255, 255, 255))
			self.screen.blit (self.console_output, (self.console_pos[0] + 10, self.console_pos[1] + 310 - (self.font.get_linesize() * m)))
				
		#get_message grabs the next object in a message queue
	def get_message(self, incoming_message_queue):
	
		# if self.on == True:
	
			# self.on = False
			
		
		if len(incoming_message_queue) != 0:
			self.message = incoming_message_queue.pop(0)

			if len(self.message_list) == self.message_list_max_size:
				self.message_list.pop(0)
				self.message_list.append(self.message)
				
		self.event = self.message[2]
		
		if self.event.type == int:
			self.damage = self.message.event
			self.message[0] + "has attacked" + self.message[1] + "for " + str(self.damage)
		
		if self.event.type == str:
			if event == "Missed":
				self.message[0] + " missed"
		
		
		
			
		
			
			
		
		
	
		
		
	
		
		
