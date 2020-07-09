import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtCore
from PIL.ImageQt import ImageQt
from PIL import Image

import screengrab
import upscaler


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 image - pythonspot.com"
        self.left = 100
        self.top = 10
        self.width = 640
        self.height = 480
        self.screengrabber = screengrab.ScreenGrabber(10, 10, 300, 300)
        self.upscaler = upscaler.Upscaler()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel(self)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.show_image)
        timer.start(40)
        self.show_image()

    def show_image(self):
        img = self.pil2pixmap(self.upscaler.upscale(2, self.screengrabber.get_image()))
        self.label.setPixmap(img)
        self.resize(img.width(), img.height())

    def pil2pixmap(self, im):
        if im.mode == "RGB":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
        elif im.mode == "RGBA":
            r, g, b, a = im.split()
            im = Image.merge("RGBA", (b, g, r, a))
        elif im.mode == "L":
            im = im.convert("RGBA")
        # Bild in RGBA konvertieren, falls nicht bereits passiert
        im2 = im.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
        pixmap = QPixmap.fromImage(qim)
        return pixmap


app = QApplication(sys.argv)
window = App()
window.show()
app.exec_()
