#coding: UTF-8

import numpy as np
import cv
import cv2
from PIL import Image

image = cv2.imread("sample.tif", 0)
cv2.imshow("original", image)
cv2.waitKey(0)
cv2.destroyWindow()
