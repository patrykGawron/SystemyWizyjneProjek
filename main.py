import cv2
import numpy as np
import sys
from os import listdir


class App:
    def __init__(self, path_to_images, path_to_json):
        self.path_to_images = path_to_images
        self.path_to_json = path_to_json
        self.img_grayscale: np.ndarray = np.ndarray([])

    def load_image(self, filename):
        self.img_grayscale: np.ndarray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    def process_image(self):
        cv2.namedWindow("Test", cv2.WINDOW_NORMAL)
        cv2.imshow("Test", self.img_grayscale)
        cv2.waitKey()

    def run(self):
        for f in sorted(listdir(self.path_to_images)):
            self.load_image(f"{self.path_to_images}/{f}")
            self.process_image()


if __name__ == "__main__":
    app = App(sys.argv[1], sys.argv[2])
    app.run()
