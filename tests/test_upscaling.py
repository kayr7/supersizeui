import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from supersize import upscaler
from supersize import ganupscaler

from PIL import Image


def test_upscaler():
    ups = upscaler.Upscaler()
    img = Image.open("./box.png")
    new_img = ups.upscale(img, 2)
    assert new_img.width == 2 * img.width
    assert new_img.height == 2 * img.height
    img.close()


def test_gan_upscale():
    img = Image.open("./box.png")
    upsc = ganupscaler.GanUpscaler()
    assert upsc.model is not None
    up_img = upsc.upscale(img)

    assert up_img.width == 4 * img.width and up_img.height == 4 * img.height
    img.close()
    up_img.save("temp.jpg")
    up_img.close()

