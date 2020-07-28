import numpy as np
import cv2
import imutils


class colordescriptor:
    def __init__(self, bins):
        self.bins = bins
    def Histogram(self, image, mask):
            Hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,
                [0, 180, 0, 256, 0, 256])
            if imutils.is_cv2():
                Hist = cv2.normalize(Hist).flatten()
            else:
                Hist = cv2.normalize(Hist, Hist).flatten()
            return Hist

    def describe(self, Image):
        Image = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
        features = []
        (h, w) = Image.shape[:2]
        (cX, cY) = (int(w * 0.5), int(h * 0.5))
        segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),(0, cX, cY, h)]

        (axesX, axesY) = (int(w * 0.5) // 2, int(h * 0.5) // 2)
        ellipMask = np.zeros(Image.shape[:2], dtype="uint8")
        cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)


        for (startX, endX, startY, endY) in segments:
            cornerMask = np.zeros(Image.shape[:2], dtype="uint8")
            cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
            cornerMask = cv2.subtract(cornerMask, ellipMask)
            hist = self.Histogram(Image, cornerMask)

            features.extend(hist)

        hist = self.Histogram(Image, ellipMask)
        features.extend(hist)

        return features

