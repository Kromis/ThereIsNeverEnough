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
			self.screen.blit (self.console_output, (self.console_pos[0] + 5, self.console_pos[1] + 10 + (self.font.get_linesize() * m)))
				
	#get_message grabs the next object in a message queue
	def get_message(self, incoming_message_queue):
                if len(incoming_message_queue) != 0:
                        self.time = '[' + '{:02d}:{:02d}'.format(resources.time.hour, resources.time.minute) + '] '
                        self.message = incoming_message_queue.pop(0)
                        self.event = self.message[2]
                        
                        if type(self.event) == int:
                                self.damage = self.event
                                self.message = [self.time + self.message[0] + " has attacked " + self.message[1] + " for " + str(self.event)]
                        
                        if type(self.event) == str:
                                if self.event == "Missed":
                                        self.message = [self.time + self.message[0] + " missed."]
                                if self.event == "Damaged" or self.event == "Flavor":
                                        self.message = [self.time + self.message[3]]

                        print("Text to be sanitized: " + self.message[0])
                        self.message = self.sanitize(self.message[0])
                       
                            
                        for m in range(len(self.message)):                            
                            self.message_list.append(self.message[m])
                        
                        while len(self.message_list) >= self.message_list_max_size:
                                self.message_list.pop(0)

	def sanitize(self, message):
		self.message_split = []
		self.message = message
		print("Checking text size = " + str((self.font.size(self.message))[0]))

		#If the message to be sanitized is greater than 630 pixels wide...
		if self.font.size(self.message)[0] > 630:
			self.temp_split = self.message.split()
			self.temp_join = ""
			self.temp_join2 = ""
			#Split self.message and add each word one by one to a new string
			for s in range(len(self.temp_split)):
				if self.temp_join == "":
                                        self.temp_join = s
				else:
                                        #temp_join2 is a copy of temp_join before a word is added to temp_join
                                        #if a word is added to temp_join and the entire string is longer than 630 pixels
                                        #then append temp_join2

					self.temp_join2 = self.temp_join
					self.temp_join = " ".join([str(self.temp_join), self.temp_split[s]])
					print(self.font.size(self.temp_join)[0])
					print(self.temp_join)

					#This checks if temp_join is longer than 630 pixels; if it is, append temp_join2
					if self.font.size(self.temp_join)[0] >= 630:
                                        	print("New line = " + self.temp_join2)
                                        
                                        	self.temp_join = " ".join(self.temp_split[s:])
                                        	self.message_split.append(self.temp_join2)
                                        	self.sanitize(self.temp_join)
                                        	break
                                                
		else:
                        self.message_split.append(message)
		return self.message_split
        
