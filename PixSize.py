# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import requests
from io import BytesIO
from PIL import Image

url = 'https://raw.githubusercontent.com/adtacharya/pix-modulation-functions/main/camera.png'
response = requests.get(url)
bwPhoto = Image.open(BytesIO(response.content)).convert('L')
bwPhoto = np.array(bwPhoto) 
bwPhoto = bwPhoto.astype(np.float64)

url = 'https://raw.githubusercontent.com/adtacharya/pix-modulation-functions/main/CameraBlur.png'
response = requests.get(url)
blurPhoto = Image.open(BytesIO(response.content)).convert('L')
blurPhoto = np.array(blurPhoto) 
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

def ESF(pixel,a,b,c,d):
    """
    Compute the Edge Spread Function from given parameters
    """
    esf = a/(np.exp((pixel-b)/c)+1)+d

    return esf

parameters, covarience = curve_fit(ESF,pixel,selected_line)
a = parameters[0]
b = parameters[1]
c = parameters[2]
d = parameters[3]

par, covar = curve_fit(ESF,pixel,selected_line1)
a1 = par[0]
b1 = par[1]
c1 = par[2]
d1 = par[3]

esf =  a/(np.exp((pixel-b)/c)+1)+d
esf1 =  a1/(np.exp((pixel-b1)/c1)+1)+d1

plt.figure()
plt.plot(pixel,selected_line,'.',pixel,esf,pixel,selected_line1,'.',pixel,esf)
plt.title("Edge Spread Function (ESF)")
plt.ylabel("Pixel Intensity")
plt.xlabel("Pixel Number")

esf = a/(np.exp((pixel-b)/c)+1)+d
esf1 = a1/(np.exp((pixel-b1)/c1)+1)+d1

LSF_nu = abs(np.diff(esf))
LSF_nu1 = abs(np.diff(esf1))

LSF_an = abs(a*np.exp((pixel-b)/c)/(c*(np.exp((pixel-b)/c)+1)**2))
LSF_an1 = abs(a1*np.exp((pixel-b1)/c1)/(c1*(np.exp((pixel-b1)/c1)+1)**2))

LSF_ave = np.mean(np.vstack((np.append(LSF_nu,0), LSF_an)),0)
LSF_ave1 = np.mean(np.vstack((np.append(LSF_nu1,0), LSF_an1)),0)

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
