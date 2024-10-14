import pygame
import psycopg2
from simulation.population import Population
from datetime import datetime

START_TIME = 0
END_TIME = 0
TOTAL_INFECTED_TIME = 0
AVG_INFECTION_TIME = 0
P30_TIME = 0
P50_TIME = 0
P70_TIME = 0
PEAK_INCUBATING = 0
PEAK_INFECTED = 0
PERSON_SPEED = 0
SUM_OF_POPULATION = 0

DB_NAME = 'postgres'
USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'


class Statistics:
    """
    Class containing statistics about a population
    """
    def __init__(self):
        self.start_time = START_TIME
        self.end_time = END_TIME
        self.total_infected_time = TOTAL_INFECTED_TIME
        self.avg_infection_time = AVG_INFECTION_TIME
        self.p30_time = P30_TIME
        self.p50_time = P50_TIME
        self.p70_time = P70_TIME
        self.peak_incubating = PEAK_INCUBATING
        self.peak_infected = PEAK_INFECTED
        self.game_date = datetime.now()
        self.speed = PERSON_SPEED
        self.sum_of_population = SUM_OF_POPULATION

    def start_time(self) -> None:
        """
        Return the start time of the statistics calculation.
        """
        self.start_time = pygame.time.get_ticks()

    def format_date(self):
        """
        Format the time of the statistics calculation.
        :return: current time and date in format
        """
        current_date = self.game_date.strftime('%Y-%m-%d')
        current_time = self.game_date.strftime('%H:%M:%S')
        return current_date, current_time

    def update_statistics(self, population: Population) -> None:
        """
        Update the statistics based on a population.
        :param population:
        """
        current_time = pygame.time.get_ticks() - self.start_time

        infected_count = population.get_infected_count()

        if infected_count / len(population.people) >= 0.3 and self.p30_time == 0:
            self.p30_time = current_time
        if infected_count / len(population.people) >= 0.5 and self.p50_time == 0:
            self.p50_time = current_time
        if infected_count / len(population.people) >= 0.7 and self.p70_time == 0:
            self.p70_time = current_time

        incubating_count = population.get_incubation_count()
        if incubating_count > self.peak_incubating:
            self.peak_incubating = incubating_count

        if infected_count > self.peak_infected:
            self.peak_infected = infected_count

    def end_game(self, population: Population) -> None:
        """
        Collect statistics
        :param population:
        """
        self.end_time = pygame.time.get_ticks() - self.start_time

        total_infected_time = self.end_time
        avg_infection_time = total_infected_time / len(population.people)

        self.total_infected_time = total_infected_time
        self.avg_infection_time = avg_infection_time

    def save_statistics_into_text_file(self, filename='statistics.txt') -> None:
        """
        Save statistics to a text file.
        :param filename:
        """
        with open(filename, 'a') as f:
            f.write("-----------------------------------")
            f.write("\n")
            f.write(f"Game date: {self.format_date()}\n")
            f.write(f"Total infected time: {self.total_infected_time} ms\n")
            f.write(f"Average infection time: {self.avg_infection_time} ms\n")
            f.write(f"30% infected at: {self.p30_time} ms\n")
            f.write(f"50% infected at: {self.p50_time} ms\n")
            f.write(f"70% infected at: {self.p70_time} ms\n")
            f.write(f"Peak incubating: {self.peak_incubating}\n")
            f.write(f"Peak infected: {self.peak_infected}\n")

    @staticmethod
    def create_table() -> None:
        """
        Create a table of statistics.
        """
        with psycopg2.connect(
                dbname=DB_NAME,
                user=USER,
                password=PASSWORD,
                host=HOST
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS statistics (
                        id serial PRIMARY KEY,
                        total_infected CHARACTER VARYING(115),
                        average_infection_time CHARACTER VARYING(115),
                        p30_time CHARACTER VARYING(115),
                        p50_time CHARACTER VARYING(115),
                        p70_time CHARACTER VARYING(115),
                        peak_incubating INTEGER,
                        peak_infected INTEGER
                    )
                """)

    @staticmethod
    def save_statistics_into_database(statistics) -> None:
        """
        Save statistics to a database.
        """
        with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO statistics (
                        total_infected,
                        average_infection_time,
                        p30_time,
                        p50_time,
                        p70_time,
                        peak_incubating,
                        peak_infected
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s
                    )
                    """,
                    (
                        str(statistics.total_infected_time),
                        str(statistics.avg_infection_time),
                        str(statistics.p30_time),
                        str(statistics.p50_time),
                        str(statistics.p70_time),
                        statistics.peak_incubating,
                        statistics.peak_infected
                    )
                )
