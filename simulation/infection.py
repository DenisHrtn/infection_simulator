class Infection:
    def __init__(self, population):
        self.population = population

    def update(self) -> None:
        for person in self.population.people:
            if person.is_incubating():
                person.update_health_status()
