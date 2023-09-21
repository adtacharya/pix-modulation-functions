# Author: Andrew Fleck
# 09/21/23

import numpy as np
import matplotlib.pyplot as plt

# downloads black and white photo
bwPhoto = plt.imread('Camera.png')
bwPhoto = np.double(bwPhoto[:,:,0])

# downloads tissue covered photo
tisPhoto = plt.imread('CameraBlur.png')
tisPhoto = np.double(tisPhoto[:,:,0])

# Plots both black and white photo and tissue photos
fig, axs = plt.subplots(2, 1)
axs[0].imshow(bwPhoto, cmap='gray')
axs[0].set_title('Image Pixel Data')
axs[0].set_xlabel('Pixel Count (x-direction)')
axs[0].set_ylabel('Pixel Count (y-direction)')
axs[1].imshow(tisPhoto, cmap='gray')
axs[1].set_xlabel('Pixel Count (x-direction)')
axs[1].set_ylabel('Pixel Count (y-direction)')

# Creates x and y data for the pixels and their outputs
selected_line = bwPhoto[139:215,209]
selected_line1 = tisPhoto[142:218,209]
pixel = np.arange(1, 77)

# Best fit for the black and white photo
# Parameters 
a = 166.2
b = 33.14
c = 0.6217
d = 16.17

# Best fit for the tissue photo
a1 = 168.3
b1 = 33.35
c1 = 3.508
d1 = 14.46

# Models for both black and white photo and tissue photo
line_mod =  a/(np.exp((pixel-b)/c)+1)+d
line_mod1 =  a1/(np.exp((pixel-b1)/c1)+1)+d1

# Plots ESF for both photos as well as models on same plot
plt.figure()
plt.plot(pixel, selected_line, '.')
plt.plot(pixel, selected_line1, '.')
plt.plot(pixel, line_mod)
plt.plot(pixel, line_mod1)
plt.title('Edge Spread Function (ESF)')
plt.xlabel('Pixel Number')
plt.ylabel('Pixel Output')
plt.legend(['Control', 'Distortion', 'Control Model', 'Distortion Model'])

plt.show()