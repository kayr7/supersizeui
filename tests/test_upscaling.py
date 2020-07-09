import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from supersize import upscaler

from PIL import Image


def test_upscaler():
    ups = upscaler.Upscaler()
    img = Image.open("./box.png")
    new_img = ups.upscale(2, img)
    assert new_img.width == 2 * img.width
    assert new_img.height == 2 * img.height
    img.close()
