# Specify device
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"

import sys
import cv2

# NomeroffNet path
NOMEROFF_NET_DIR = os.path.abspath('../../')

sys.path.append(NOMEROFF_NET_DIR)

# Import license plate recognition tools.
from license_plate_analyzer.NomeroffNet.YoloV5Detector import Detector
detector = Detector()
detector.load()

from license_plate_analyzer.NomeroffNet import TextDetector
from license_plate_analyzer.NomeroffNet import textPostprocessing


class PlateAnalyzer:
    file_path_base = ''

    def __init__(self):
        self.textDetector = TextDetector.get_static_module("eu")()
        self.textDetector.load("latest")
        self.zones = []
        self.region_names = []

    def _fill_zones_and_regions(self, image):
        targetBoxes = detector.detect_bbox(image)

        for targetBox in targetBoxes:
            x = int(min(targetBox[0], targetBox[2]))
            w = int(abs(targetBox[2]-targetBox[0]))
            y = int(min(targetBox[1], targetBox[3]))
            h = int(abs(targetBox[3]-targetBox[1]))

            image_part = image[y:y + h, x:x + w]
            self.zones.append(image_part)
            self.region_names.append('eu')

    def get_plate_number(self, image):
        image.save(image.filename)
        img = cv2.imread(image.filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self._fill_zones_and_regions(img)
        text_array = self.textDetector.predict(self.zones)
        return textPostprocessing(text_array, self.region_names)
