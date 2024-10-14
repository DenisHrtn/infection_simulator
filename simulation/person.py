import pygame
import random
from probability.probability_calculation import ProbabilityCalculation


INCUBATION_PERIOD = 20000
INCUBATION_START_TIME = 0
PERSON_SIZE = 10
HEALTHY_COLOR = (0, 255, 0)  # green
INFECTED_COLOR = (255, 0, 0)  # red
INCUBATED_COLOR = (255, 165, 0)  # orange
PERSON_SPEED = 5


class Person:
    def __init__(self, width: int, height: int, city):
        self.width = width
        self.height = height
        self.size = PERSON_SIZE
        self.city = city
        self.rect = self.spawn_person()
        self.health_status = 'healthy'
        self.incubation_period = INCUBATION_PERIOD
        self.incubation_start_time = INCUBATION_START_TIME
        self.speed = PERSON_SPEED

    def spawn_person(self) -> pygame.rect:
        """
        Spawns a person randomly.
        :return: A person object.
        """
        new_rect = pygame.Rect(
            random.randint(0, self.width - self.size),
            random.randint(0, self.height - self.size),
            self.size,
            self.size
        )

        # Check collision with houses
        while any(house.colliderect(new_rect) for house in self.city.houses):
            new_rect = pygame.Rect(
                random.randint(0, self.width - self.size),
                random.randint(0, self.height - self.size),
                self.size,
                self.size
            )

        return new_rect

    def move(self) -> None:
        """
        Moves the person randomly.
        """
        dx = random.choice([-self.speed, 0, self.speed])
        dy = random.choice([-self.speed, 0, self.speed])

        new_rect = self.rect.move(dx, dy)

        # Check collision with houses
        if all(not house.colliderect(new_rect) for house in self.city.houses):
            if (0 <= new_rect.left and new_rect.right < self.width and 0 <= new_rect.top and
                    new_rect.bottom < self.height):
                self.rect = new_rect

    def contact_with(self, other_person):
        """
        Checks if the person is contacted with another person.
        :param other_person:
        """
        if other_person.is_infected() and not self.is_infected() and not self.is_incubating():
            distance = pygame.math.Vector2(self.rect.center).distance_to(other_person.rect.center)
            if ProbabilityCalculation.infect_probability(distance, self.health_status):
                self.start_incubation()

    def update_health_status(self):
        """
        Updates the healthy status of the person.
        """
        if self.is_incubating():
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.incubation_start_time
            if elapsed_time >= self.incubation_period:

                # Distance is 0 as it is not needed here
                if ProbabilityCalculation.infect_probability(0, self.health_status):
                    self.infect()
                else:
                    self.health_status = 'healthy'

    def infect(self) -> None:
        """
        Infects the person.
        """
        self.health_status = 'infected'

    def is_infected(self):
        """
        If the person is infected.
        :return: Health status of the person.
        """
        return self.health_status == 'infected'

    def start_incubation(self) -> None:
        """
        Starts the incubation period.
        """
        self.health_status = 'incubating'
        self.incubation_start_time = pygame.time.get_ticks()

    def is_incubating(self):
        """
        If the person is infected.
        :return: Health status of the person.
        """
        return self.health_status == 'incubating'

    def draw(self, screen) -> pygame.rect:
        """
        Draws the person.
        :param screen:
        """
        color = HEALTHY_COLOR
        if self.is_infected():
            color = INFECTED_COLOR
        elif self.is_incubating():
            color = INCUBATED_COLOR

        pygame.draw.rect(screen, color, self.rect)
