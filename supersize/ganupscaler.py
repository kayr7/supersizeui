from tensorflow import keras
import numpy as np
import os
from numpy import asarray
from PIL import Image


class GanUpscaler:
    def __init__(self):
        self.Model = None
        self.load_model("supersize/FAST-SRGAN/models/generator.h5")
        pass

    def load_model(self, file):
        self.model = keras.models.load_model(file)
        self.inputs = keras.Input((None, None, 3))
        self.output = self.model(self.inputs)
        self.model = keras.models.Model(self.inputs, self.output)

    def upscale(self, img):
        pic = asarray(img)
        pic = pic.astype("float32")
        pic /= 255.0
        sr = self.model.predict(np.expand_dims(pic, axis=0))[0]
        sr = ((sr + 1) / 2.0) * 255
        ret_img = Image.fromarray(np.uint8(sr))
        return ret_img

