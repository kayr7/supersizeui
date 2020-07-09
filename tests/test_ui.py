import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from supersize import screengrab

from time import process_time
import pytest


def NOTONGITHUBtest_screengrabber():
    screengrabber = screengrab.ScreenGrabber(10, 10, 100, 100)
    im = screengrabber.get_image()
    assert im.width == 90
    assert im.height == 90
    im.save("box.png")
    assert os.path.isfile("box.png")
    im.close()


def NOTONGITHUBtest_screengrabber_iteration():
    screengrabber = screengrab.ScreenGrabber(10, 10, 100, 100)
    t = process_time()
    for _ in range(100):
        im = screengrabber.get_image()
    elapsed_time = process_time() - t
    assert elapsed_time / 100.0 < 0.04
    print(elapsed_time / 100)

