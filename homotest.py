import os
import time
import json
from datetime import date, datetime
import zlib
import queue
import hashlib
import uuid

import numpy as np

import cv2

tel_1 = cv2.resize(cv2.imread('./temp/tel_5.jpg', cv2.IMREAD_GRAYSCALE),(360,640))
tel_2 = cv2.resize(cv2.imread('./temp/tel_6.jpg', cv2.IMREAD_GRAYSCALE),(360,640))

BRISK = cv2.BRISK_create()
keypoints1, descriptors1 = BRISK.detectAndCompute(tel_1, None)
keypoints2, descriptors2 = BRISK.detectAndCompute(tel_2, None)

# create BFMatcher object
BFMatcher = cv2.BFMatcher(normType = cv2.NORM_HAMMING, crossCheck = True)

# Matching descriptor vectors using Brute Force Matcher
matches = BFMatcher.match(queryDescriptors = descriptors1, trainDescriptors = descriptors2)


# Sort them in the order of their distance
matches = sorted(matches, key = lambda x: x.distance)

# Draw first 15 matches
output = cv2.drawMatches(img1 = tel_1,
                        keypoints1 = keypoints1,
                        img2 = tel_2,
                        keypoints2 = keypoints2,
                        matches1to2 = matches[:15],
                        outImg = None,
                        flags = cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv2.imshow('output', output)
cv2.waitKey(0)

'''
tel_1 = cv2.imread('./temp/tel_1.jpg', cv2.IMREAD_GRAYSCALE)
surf = cv2.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(tel_1,None)
tel_1_kp = cv2.drawKeypoints(tel_1,kp,None,(255,0,0),4)
cv2.imshow('tel_1_kp', tel_1_kp)
cv2.waitKey(0)

cv2.imshow('tel_1', tel_1)
cv2.imshow('tel_2', tel_2)
'''
