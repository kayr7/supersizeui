import pyscreenshot as ImageGrab



class ScreenGrabber():
    def __init__(self, x1, y1, x2, y2):
        self.bbox = (x1, y1, x2, y2)

    def get_image(self):
        return ImageGrab.grab(self.bbox, backend="mss", childprocess=False)

    