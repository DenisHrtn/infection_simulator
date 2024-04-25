import pygame
import sys


class StartScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont(None, 50)
        self.title_font = pygame.font.SysFont(None, 80)
        self.start_button = pygame.Rect(self.width // 2 - 100, 200, 200, 50)
        self.exit_button = pygame.Rect(self.width // 2 - 100, 300, 200, 50)
        self.running = True
        self.selected = None

    def draw(self):
        self.screen.fill((255, 255, 255))

        title_text = self.title_font.render("Infection Simulator", True, (0, 0, 0))
        self.screen.blit(title_text, (self.width // 2 - title_text.get_width() // 2, 100))

        start_text = self.font.render("Start", True, (0, 0, 0))
        pygame.draw.rect(self.screen, (0, 255, 0) if self.selected == 'start' else (0, 150, 0), self.start_button)
        self.screen.blit(start_text, (self.width // 2 - start_text.get_width() // 2, 210))

        exit_text = self.font.render("Exit", True, (0, 0, 0))
        pygame.draw.rect(self.screen, (255, 0, 0) if self.selected == 'exit' else (150, 0, 0), self.exit_button)
        self.screen.blit(exit_text, (self.width // 2 - exit_text.get_width() // 2, 310))

        author_text = self.font.render("Created by Kharytonchyk Dzianis", True, (0, 0, 0))
        self.screen.blit(author_text, (self.width // 2 - author_text.get_width() // 2, 500))

        text = self.font.render("2024", True, (0, 0, 0))
        self.screen.blit(text, (self.width // 2 - text.get_width() // 2, 550))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if self.start_button.collidepoint(x, y):
                    self.running = False
                elif self.exit_button.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                self.selected = None
                if self.start_button.collidepoint(x, y):
                    self.selected = 'start'
                elif self.exit_button.collidepoint(x, y):
                    self.selected = 'exit'

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
