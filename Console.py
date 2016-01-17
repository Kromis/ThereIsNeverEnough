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
		self.message = []
		self.event = None
		self.time = None
		self.message_list = []
		self.message_list_max_size = 10
		self.console_pos = (628, 30)
		
	def draw(self):
		self.screen.blit(self.console_img, self.console_pos)
		for m in range(len(self.message_list)):
			self.console_output = self.font.render(self.message_list[m], True, pygame.Color(255, 255, 255))
			self.screen.blit (self.console_output, (self.console_pos[0] + 10, self.console_pos[1] + (self.font.get_linesize() * m)))
				
		#get_message grabs the next object in a message queue
	def get_message(self, incoming_message_queue):
                if len(incoming_message_queue) != 0:
                        self.time = '[' + '{:02d}:{:02d}'.format(resources.time.hour, resources.time.minute) + '] '
                        self.message = incoming_message_queue.pop(0)
                        self.event = self.message[2]

                        if type(self.event) == int:
                                self.damage = self.event
                                self.message = self.time + self.message[0] + " has attacked " + self.message[1] + " for " + str(self.event)
                        
                        if type(self.event) == str:
                                if event == "Missed":
                                        self.message = self.time + self.message[0] + " missed."

                        self.message_list.append(self.message)
                        
                        if len(self.message_list) >= self.message_list_max_size:
                                self.message_list.pop(0)
		
		
		
			
		
			
			
		
		
	
		
		
	
		
		
