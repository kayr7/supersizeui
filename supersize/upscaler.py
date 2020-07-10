from PIL import Image


class Upscaler:
    def __init__(self):
        pass

    def upscale(self, image: Image, factor: int = 2):
        new_image = image.resize(
            (int(image.width * factor), int(image.height * factor))
        )
        return new_image
