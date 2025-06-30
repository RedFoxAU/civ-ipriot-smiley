from smiley import Smiley

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)  # Set the complexion to RED
        self.draw_mouth()
        self.draw_eyes()
        """
        Provides a Smiley with a Angry expression
        """
    def draw_mouth(self):
        mouth = [41, 46, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        eyes = [10, 18, 22, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()

    def blink(self, delay=0):  # Placeholder for future feature
        pass