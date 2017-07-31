# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 19:30:44 2017

@author: Shabaka
"""

import matplotlib.pyplot as plt
import numpy as np

# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Display the image
plt.imshow(img)

# Hide the axes
plt.axis('off')
plt.show()

# ''''''''''' Pseudocolor Plot from Image Data ''''''''''''#

# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Compute the sum of the red, green and blue channels: intensity
intensity = img.sum(axis=2)

# Print the shape of the intensity
print(intensity.shape)

# Display the intensity with a colormap of 'gray'
plt.imshow(intensity, cmap='gray')

# Add a colorbar
plt.colorbar()

# Hide the axes and show the figure
plt.axis('off')
plt.show()

# # '''''''''''''Specifying Extents and Aspect Ratio '''''#

# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')

# Specify the extent and aspect ratio of the top left subplot
plt.subplot(2, 2, 1)
plt.title('extent=(-1,1,-1,1),\naspect=0.5')
plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])
plt.imshow(img, extent=(-1, 1, -1, 1), aspect=0.5)

# Specify the extent and aspect ratio of the top right subplot
plt.subplot(2, 2, 2)
plt.title('extent=(-1,1,-1,1),\naspect=1')
plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])
plt.imshow(img, extent=(-1, 1, -1, 1), aspect=1)

# Specify the extent and aspect ratio of the bottom left subplot
plt.subplot(2, 2, 3)
plt.title('extent=(-1,1,-1,1),\naspect=2')
plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])
plt.imshow(img, extent=(-1, 1, -1, 1), aspect=2)

# Specify the extent and aspect ratio of the bottom right subplot
plt.subplot(2, 2, 4)
plt.title('extent=(-2,2,-1,1),\naspect=2')
plt.xticks([-2, -1, 0, 1, 2])
plt.yticks([-1, 0, 1])
plt.imshow(img, extent=(-2, 2, -1, 1), aspect=2)

# Improve spacing and display the figure
plt.tight_layout()
plt.show()

# '''''' Rescale Pixel Intensities '''''''''''''#

# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

# Extract minimum and maximum values from the image: pmin, pmax
pmin, pmax = image.min(), image.max()
print("The smallest & largest pixel intensities are %d & %d." % (pmin, pmax))

# Rescale the pixels: rescaled_image
rescaled_image = 256*(image - pmin) / (pmax - pmin)
print("The rescaled smallest & largest pixel intensities are %.1f & %.1f." %
      (rescaled_image.min(), rescaled_image.max()))

# Display the original image in the top subplot
plt.subplot(2, 1, 1)
plt.title('original image')
plt.axis('off')
plt.imshow(image, extent=(-2, 2, -1, 1), aspect=2)

# Display the rescaled image in the bottom subplot
plt.subplot(2, 1, 2)
plt.title('rescaled image')
plt.axis('off')
plt.imshow(rescaled_image, extent=(-2, 2, -1, 1), aspect=2)

plt.show()