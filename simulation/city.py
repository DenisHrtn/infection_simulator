import pygame


HOUSE_COLOR = (100, 100, 100)
WINDOW_COLOR = (0, 0, 255, 255)
DOOR_COLOR = (190, 190, 190, 255)
BLACK_COLOR = (0, 0, 0, 255)
WHITE_COLOR = (255, 255, 255, 255)


class City:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.houses = [
            pygame.Rect(50, 50, 100, 100),
            pygame.Rect(5, 190, 60, 110),
            pygame.Rect(200, 100, 100, 60),
            pygame.Rect(260, 50, 40, 60),
            pygame.Rect(200, 200, 80, 120),
            pygame.Rect(400, 100, 120, 90),
            pygame.Rect(600, 300, 110, 100),
            pygame.Rect(410, 280, 40, 40),
            pygame.Rect(410, 240, 40, 40),
            pygame.Rect(410, 320, 40, 40),
            pygame.Rect(450, 280, 40, 40),
            pygame.Rect(370, 280, 40, 40),
            pygame.Rect(100, 400, 130, 70),
            pygame.Rect(5, 500, 50, 50),
            pygame.Rect(500, 500, 130, 80),
            pygame.Rect(300, 400, 90, 100),
            pygame.Rect(700, 150, 100, 110),
            pygame.Rect(540, 110, 110, 110)
        ]

        self.windows = [
            pygame.Rect(60, 65, 20, 20),
            pygame.Rect(90, 65, 20, 20),
            pygame.Rect(120, 65, 20, 20),
            pygame.Rect(60, 90, 20, 20),
            pygame.Rect(90, 90, 20, 20),
            pygame.Rect(120, 90, 20, 20),
            pygame.Rect(60, 115, 20, 20),
            pygame.Rect(120, 115, 20, 20),
            pygame.Rect(10, 200, 20, 20),
            pygame.Rect(40, 200, 20, 20),
            pygame.Rect(10, 225, 20, 20),
            pygame.Rect(40, 225, 20, 20),
            pygame.Rect(10, 250, 20, 15),
            pygame.Rect(40, 250, 20, 15),
            pygame.Rect(270, 55, 20, 20),
            pygame.Rect(270, 80, 20, 20),
            pygame.Rect(270, 105, 20, 16),
            pygame.Rect(241, 105, 20, 16),
            pygame.Rect(213, 105, 20, 16),
            pygame.Rect(270, 130, 20, 16),
            pygame.Rect(213, 130, 20, 16),
            pygame.Rect(210, 215, 20, 20),
            pygame.Rect(248, 215, 20, 20),
            pygame.Rect(210, 245, 20, 20),
            pygame.Rect(248, 245, 20, 20),
            pygame.Rect(410, 115, 20, 20),
            pygame.Rect(450, 115, 20, 20),
            pygame.Rect(490, 115, 20, 20),
            pygame.Rect(410, 145, 20, 20),
            pygame.Rect(490, 145, 20, 20),
            pygame.Rect(610, 315, 20, 20),
            pygame.Rect(645, 315, 20, 20),
            pygame.Rect(680, 315, 20, 20),
            pygame.Rect(610, 345, 20, 20),
            pygame.Rect(680, 345, 20, 20),
            pygame.Rect(107, 415, 20, 20),
            pygame.Rect(139, 415, 20, 20),
            pygame.Rect(171, 415, 20, 20),
            pygame.Rect(203, 415, 20, 20),
            pygame.Rect(9, 510, 10, 10),
            pygame.Rect(24, 510, 10, 10),
            pygame.Rect(39, 510, 10, 10),
            pygame.Rect(9, 525, 10, 10),
            pygame.Rect(39, 525, 10, 10),
            pygame.Rect(510, 515, 20, 20),
            pygame.Rect(540, 515, 20, 20),
            pygame.Rect(570, 515, 20, 20),
            pygame.Rect(600, 515, 20, 20),
            pygame.Rect(510, 545, 20, 20),
            pygame.Rect(600, 545, 20, 20),
            pygame.Rect(315, 415, 20, 20),
            pygame.Rect(355, 415, 20, 20),
            pygame.Rect(315, 445, 20, 20),
            pygame.Rect(355, 445, 20, 20),
            pygame.Rect(705, 165, 20, 20),
            pygame.Rect(740, 165, 20, 20),
            pygame.Rect(775, 165, 20, 20),
            pygame.Rect(705, 195, 20, 20),
            pygame.Rect(740, 195, 20, 20),
            pygame.Rect(775, 195, 20, 20),
            pygame.Rect(545, 125, 20, 20),
            pygame.Rect(585, 125, 20, 20),
            pygame.Rect(625, 125, 20, 20),
            pygame.Rect(545, 155, 20, 20),
            pygame.Rect(585, 155, 20, 20),
            pygame.Rect(625, 155, 20, 20),
            pygame.Rect(545, 185, 20, 20),
            pygame.Rect(625, 185, 20, 20),
        ]

        self.doors = [
            pygame.Rect(92.7, 115, 15, 35),
            pygame.Rect(28.7, 268, 12, 32),
            pygame.Rect(245, 125, 15, 35),
            pygame.Rect(232, 285, 15, 35),
            pygame.Rect(452, 155, 15, 35),
            pygame.Rect(648, 365, 15, 35),
            pygame.Rect(157, 440, 14, 30),
            pygame.Rect(24, 528, 10, 22),
            pygame.Rect(556, 547, 13, 33),
            pygame.Rect(338.7, 470, 13, 30),
            pygame.Rect(744, 230, 15, 30),
            pygame.Rect(587, 190, 15, 30),
        ]

        self.knobs = [
            pygame.Rect(102, 130, 3, 3),
            pygame.Rect(35, 280, 3, 3),
            pygame.Rect(255, 140, 3, 3),
            pygame.Rect(242, 300, 3, 3),
            pygame.Rect(462, 170, 3, 3),
            pygame.Rect(658, 380, 3, 3),
            pygame.Rect(167, 455, 3, 3),
            pygame.Rect(30, 538, 2, 2),
            pygame.Rect(564, 562, 3, 3),
            pygame.Rect(347.5, 485, 3, 3),
            pygame.Rect(754, 245, 3, 3),
            pygame.Rect(597, 205, 3, 3),
        ]

        self.square = [
            pygame.Rect(418, 285, 5, 30),
            pygame.Rect(438, 285, 5, 30),
            pygame.Rect(420, 297, 20, 5),
        ]

    def draw(self, screen) -> None:
        """
        Draws the city on the screen.
        :param screen:
        """
        for house in self.houses:
            pygame.draw.rect(screen, HOUSE_COLOR, house)

        for window in self.windows:
            pygame.draw.rect(screen, WINDOW_COLOR, window)

        for door in self.doors:
            pygame.draw.rect(screen, DOOR_COLOR, door)

        for knob in self.knobs:
            pygame.draw.rect(screen, BLACK_COLOR, knob)

        pygame.draw.circle(screen, DOOR_COLOR, (430, 300), 25, 0)

        for square in self.square:
            pygame.draw.rect(screen, WHITE_COLOR, square)
