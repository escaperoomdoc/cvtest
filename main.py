import os
import time
import json
from datetime import date, datetime
import zlib
import queue
import hashlib
import uuid

from dotenv import load_dotenv

import cv2

def go_blur():
    img = cv2.imread('./temp/pic_1.jpeg', cv2.IMREAD_GRAYSCALE)
    blur = cv2.blur(img,(5,5))
    cv2.imshow('blur', blur)
    cv2.waitKey(0)


def go_canny():
    img = cv2.imread('./temp/pic_1.jpeg', cv2.IMREAD_GRAYSCALE)
    canny = cv2.Canny(img,100,200)
    cv2.imshow('canny', canny)
    cv2.waitKey(0)

go_blur()
go_canny()

