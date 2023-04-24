import pygame


class Q_frame():
    def __init__(self, screen, loctextX, loctextY, content):
        self.screen = screen
        self.loctextX = loctextX
        self.loctextY = loctextY
        self.content = content

    def display_textbox(self):
        text_bubble = pygame.image.load('./sprites/text_bubbles.png')
        # Scale the image to your needed size
        text_bubble = pygame.transform.scale_by(text_bubble, 0.2)
        
        print(self.loctextX*3/5*4/6, self.loctextY*1/3*3/6)
        self.screen.blit(text_bubble, (self.loctextX*3/5*4/6, self.loctextY*1/3*3/6))

    def add_characters(self):
        character = pygame.image.load('./sprites/character/Ask_Me_2-removebg-preview.png')
        # Scale the image to your needed size
        character = pygame.transform.scale_by(character, 0.65)
        self.screen.blit(character, (100, 300)) 

    def display(self):
        self.display_textbox()
        self.add_characters()  