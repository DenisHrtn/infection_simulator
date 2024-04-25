import random


class ProbabilityCalculation:
    @staticmethod
    def infect_probability(distance, health_status):
        """
        Calculate infection probability based on distance and health status.
        :param distance: float, distance between people
        :param health_status: str, health status of the person
        :return: bool, True if infection occurs, False otherwise
        """
        base_prob = random.random()

        # Increase probability based on proximity
        if distance < 20:
            base_prob *= 2

        # Increase probability if the other person is infected
        if health_status == 'infected':
            base_prob *= 2

        return base_prob < 0.5

    @staticmethod
    def incubation_probability():
        return random.random() < 0.5
