import time
from blinkable import Blinkable
from smiley import Smiley

class Sad(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=self.BLUE)  # Pass BLUE as the complexion# Updated from super().__init__() for 3.4 Flexiable Colours - Step 3

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.complexion()  # Changed from self.YELLOW to self.complexion()
            self.pixels[pixel] = eyes

    def blink(self, delay=0.25):  # Implement Blink in Sad class
        """
        Blinks the smiley's eyes once

        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()