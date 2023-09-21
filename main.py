import os
import time
import json
from datetime import date, datetime
import zlib
import queue
import hashlib
import uuid

from dotenv import load_dotenv
import numpy as np

import cv2

def go_blur(img_name):
    img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    blur = cv2.blur(img,(5,5))
    cv2.imshow('blur', blur)
    cv2.waitKey(0)


def go_canny(img_name):
    img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    canny = cv2.Canny(img,100,400)
    cv2.imshow('canny', canny)
    cv2.waitKey(0)

def go_filter_1(img_name):
    img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    kernel = np.ones((5,5),np.float32)/25
    print(kernel)
    dst = cv2.filter2D(img,-1,kernel)
    cv2.imshow('go_filter_1', dst)
    cv2.waitKey(0)

def go_webcam():
    webcam = cv2.VideoCapture(0)
    while True:
        ret, frame = webcam.read()
        if ret:
            canny = cv2.Canny(frame,100,200)
            cv2.imshow("tag", canny)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
    webcam.release()


# go_blur('./temp/pic_1.jpeg')
# go_canny('./temp/pic_rzd_1.png')
# go_filter_1('./temp/pic_rzd_1.png')
go_webcam()

