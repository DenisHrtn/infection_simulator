import random
from simulation.person import Person

NUMS_OF_PEOPLES = 50


class Population:
    def __init__(self, width: int, height: int, city):
        self.width = width
        self.height = height
        self.city = city
        self.people = [Person(width, height, city) for _ in range(NUMS_OF_PEOPLES)]
        self.infect_random_person()
        self.peak_incubating = 0
        self.peak_infected = 0

    def infect_random_person(self) -> None:
        """
        Infect random person
        """
        random_person = random.choice(self.people)
        random_person.infect()

    def get_infected_count(self) -> int:
        """
        Method for getting the number of infected peoples
        :return: sum of infected people (int)
        """
        return sum(1 for person in self.people if person.is_infected())

    def get_incubation_count(self) -> int:
        """
        Method for getting the number of incubated peoples
        :return: sum ofn incubated people (int)
        """
        return sum(1 for person in self.people if person.is_incubating())

    def get_health_count(self) -> int:
        """
        Method for getting the number of healthy peoples
        :return: sum of healthy people (int)
        """
        return sum(1 for person in self.people if person.health_status == 'healthy')

    def update(self) -> None:
        """
        Method for updating the population
        """
        incubating_count = self.get_incubation_count()
        infected_count = self.get_infected_count()

        if incubating_count > self.peak_incubating:
            self.peak_incubating = incubating_count

        if infected_count > self.peak_infected:
            self.peak_infected = infected_count

        for person in self.people:
            person.move()
            for other_person in self.people:
                if person != other_person and person.rect.colliderect(other_person.rect):
                    person.contact_with(other_person)
                    other_person.contact_with(person)
            person.update_health_status()

    def draw(self, screen) -> None:
        """
        Method for drawing the population
        :param screen:
        :return: pygame.Surface
        """
        for person in self.people:
            person.draw(screen)
