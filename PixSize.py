# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

bwPhoto = cv2.imread('Camera.png',cv2.IMREAD_GRAYSCALE)
bwPhoto = bwPhoto.astype(np.float64)

blurPhoto = cv2.imread('CameraBlur.png',cv2.IMREAD_GRAYSCALE)
blurPhoto = blurPhoto.astype(np.float64)

plt.figure()
fig, axs = plt.subplots(1, 2)
axs[0].imshow(bwPhoto)
axs[0].set_title("Original Photo")
axs[1].imshow(blurPhoto)
axs[1].set_title("Blurred Photo")

selected_line = bwPhoto[140:215,210]
selected_line1 = blurPhoto[143:218,210]
pixel = np.arange(1, 76,1)

a = 166.2
b = 33.14
c = 0.6217
d = 16.17

a1 = 168.3
b1 = 33.35
c1 = 3.508
d1 = 14.46

ESF =  a/(np.exp((pixel-b)/c)+1)+d
ESF1 =  a1/(np.exp((pixel-b1)/c1)+1)+d1

plt.figure()
plt.plot(pixel,selected_line,'.',pixel,ESF,pixel,selected_line1,'.',pixel,ESF)
plt.title("Edge Spread Function (ESF)")
plt.ylabel("Pixel Intensity")
plt.xlabel("Pixel Number")

ESF = a/(np.exp((pixel-b)/c)+1)+d;
ESF1 = a1/(np.exp((pixel-b1)/c1)+1)+d1;

LSF_nu = abs(np.diff(ESF));
LSF_nu1 = abs(np.diff(ESF1));

LSF_an = abs(a*np.exp((pixel-b)/c)/(c*(np.exp((pixel-b)/c)+1)**2));
LSF_an1 = abs(a1*np.exp((pixel-b1)/c1)/(c1*(np.exp((pixel-b1)/c1)+1)**2));

LSF_ave = np.mean(np.vstack((np.append(LSF_nu,0), LSF_an)),0);
LSF_ave1 = np.mean(np.vstack((np.append(LSF_nu1,0), LSF_an1)),0);

halfval = abs(0.5 - LSF_ave/max(LSF_ave))
halfval1 = abs(0.5 - LSF_ave1/max(LSF_ave1))

minVals = np.argpartition(halfval,2)

minVals1 = np.argpartition(halfval1,2)

FWHM = abs(minVals[1]-minVals[0])
FWHM1 = abs(minVals1[1]-minVals1[0])

plt.figure()
plt.plot(pixel,LSF_ave/max(LSF_ave),pixel,LSF_ave1/max(LSF_ave1))
plt.title("Line Spread Function (LSF)")
plt.ylabel("Pixel Intensity")
plt.xlabel("Pixel Number")
