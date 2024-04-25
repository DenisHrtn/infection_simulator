import pygame
import pygame.font


FONT_SIZE = 30
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0, 255, 0)
INFECTED_TEXT_COORDINATES = (10, 10)
INCUBATED_TEXT_COORDINATES = (150, 10)
HEAD_TEXT_COORDINATES = (300, 10)


class UserInterface:
    """
    Class used to represent the user interface screen.
    """
    def __init__(self, width, height, population, infection):
        self.width = width
        self.height = height
        self.population = population
        self.infection = infection
        self.font = pygame.font.SysFont(None, FONT_SIZE)

    def draw(self, screen):
        """
        Draws the user interface on the screen.
        """
        infected_count = self.population.get_infected_count()
        incubated_count = self.population.get_incubation_count()
        health_count = self.population.get_health_count()
        infected_counter = self.font.render(f"Infected: {infected_count}", True, BLACK_COLOR)
        incubated_counter = self.font.render(f"Incubated: {incubated_count}", True, BLACK_COLOR)
        health_counter = self.font.render(f"Health: {health_count}", True, BLACK_COLOR)

        screen.blit(infected_counter, INFECTED_TEXT_COORDINATES)
        screen.blit(incubated_counter, INCUBATED_TEXT_COORDINATES)
        screen.blit(health_counter, HEAD_TEXT_COORDINATES)
