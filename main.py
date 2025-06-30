"""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle."""

import time

# from happy import Happy  # Uncomment for Happy class and comment the Sad import/class.
from sad import Sad  # Swap with Happy for the Happy class.

def main():

  #  smiley = Happy()  # Uncomment for Happy class and comment the Sad import/class.

    smiley = Sad()  # Swap with Happy for the Happy class.

    smiley.show()

    time.sleep(1)

    smiley.blink()

if __name__ == '__main__':
    ############################################################
    # Uncomment the lines below only if you have multi-processing issues
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################
    main()

