from context import supersize, ScreenGrabber
import os
from time import process_time

import unittest



class TestUiMethods(unittest.TestCase):
    def test_screengrabber(self):
        screengrabber = ScreenGrabber(10,10,100,100)
        im = screengrabber.get_image()
        assert(im.width == 90)
        assert(im.height == 90)
        im.save('box.png')
        assert(os.path.isfile('box.png'))
        im.close()
        
    def test_screengrabber_iteration(self):
        screengrabber = ScreenGrabber(10,10,100,100)
        t = process_time()
        for _ in range(100):
            im = screengrabber.get_image()
        elapsed_time = process_time() - t
        assert(elapsed_time / 100. < 0.04)
        print(elapsed_time / 100)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")