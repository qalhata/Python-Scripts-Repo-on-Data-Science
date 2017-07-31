# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:56:57 2017

@author: Shabaka
"""

import numpy as np
import matplotlib.pyplot as plt

# ''''''''''' Specifying Label ''''''''''''''''#

# Specify the label 'Computer Science'
plt.plot(year, computer_science, color='red', label='Computer Science') 

# Specify the label 'Physical Sciences' 
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')

# Add a legend at the lower center
plt.legend(loc='lower center')

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()

# '''''''' ############# ;''''''''''''' ################## #

# ''''''''''''''''' Using Annotate ''''''''''''''#

# Plot with legend as before
plt.plot(year, computer_science, color='red', label='Computer Science') 
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='bottom right')

# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max = computer_science.max()

# Calculate the year in which there was maximum enrollment
# of women in Computer Science: yr_max
yr_max = year[computer_science.argmax()]

# Add a black arrow annotation
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max+5, cs_max+5),
             arrowprops=dict(facecolor='black'))

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()

# '''''''''''''''''' Modifying Plots '''''''''#

# Import matplotlib.pyplot

# Set the style to 'ggplot'
plt.style.use('ggplot')
print(plt.style.available)
# Create a figure with 2x2 subplot layout
plt.subplot(2, 2, 1) 

# Plot the enrollment % of women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Plot the enrollment % of women in Computer Science
plt.subplot(2, 2, 2)
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Add annotation

cs_max = computer_science.max()
yr_max = year[computer_science.argmax()]
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max-1,
             cs_max-10), arrowprops=dict(facecolor='black'))

# Plot the enrollmment % of women in Health professions
plt.subplot(2, 2, 3)
plt.plot(year, health, color='green')
plt.title('Health Professions')

# Plot the enrollment % of women in Education
plt.subplot(2, 2, 4)
plt.plot(year, education, color='yellow')
plt.title('Education')

# Improve spacing between subplots and display them
plt.tight_layout()
plt.show()

# '''''''''''''''' Creating a Meshed Fig ''''''''''' #

# Import numpy and matplotlib.pyplot

# Generate two 1-D arrays: u, v
u = np.linspace(-2, 2, 41)
v = np.linspace(-1, 1, 21)

# Generate 2-D arrays from u and v: X, Y
X, Y = np.meshgrid(u, v)

# Compute Z based on X and Y
Z = np.sin(3*np.sqrt(X**2 + Y**2))

# Display the resulting image with pcolor()
plt.pcolor(Z)
plt.show()

# Save the figure to 'sine_mesh.png'
plt.savefig('sine_mesh.png')


# '''''''''''' Visualising Bivariate Functions ''''''#

# ''''''''''' Contours and Filled Contours '''#

# Generate a default contour map of the array Z
plt.subplot(2, 2, 1)
plt.contour(X, Y, Z)

# Generate a contour map with 20 contours
plt.subplot(2, 2, 2)
plt.contour(X, Y, Z, 20)

# Generate a default filled contour map of the array Z
plt.subplot(2, 2, 3)
plt.contourf(X, Y, Z)

# Generate a contour map with 20 contours
plt.subplot(2, 2, 4)
plt.contourf(X, Y, Z, 20)

# Improve the spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()

# ''''''########''########''''''''''##################### #

# ''''' Colour Map Modifier ''''''''''#

# Create a filled contour plot with a color map of 'viridis'
plt.subplot(2, 2, 1)
plt.contourf(X, Y, Z, 20, cmap='viridis')
plt.colorbar()
plt.title('Viridis')

# Create a filled contour plot with a color map of 'gray'
plt.subplot(2, 2, 2)
plt.contourf(X, Y, Z, 20, cmap='gray')
plt.colorbar()
plt.title('Gray')

# Create a filled contour plot with a color map of 'autumn'
plt.subplot(2, 2, 3)
plt.contourf(X, Y, Z, 20, cmap='autumn')
plt.colorbar()
plt.title('Autumn')

# Create a filled contour plot with a color map of 'winter'
plt.subplot(2, 2, 4)
plt.contourf(X, Y, Z, 20, cmap='winter')
plt.colorbar()
plt.title('Winter')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()

# '''''''' Using hist2d() '''''''''' #

#     # Generate a 2-D histogram

_ = plt.hist2d(hp, mpg, bins=(20, 20), range=((40, 235), (8, 48)))

# Add a color bar to the histogram
_ = plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot')
plt.show()


# ''''''''''''' Plotting with hexbin() '''''''''''#

#         # Generate a 2d histogram with hexagonal bins

_ = plt.hexbin(hp, mpg, gridsize=(15, 12), extent=((40, 235, 8, 48)))

# Add a color bar to the histogram
_ = plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hexbin() plot')
plt.show()


# ''''''''''''''' Loading and Viewing Images '''''''' #

# Load the image into an array: img

img = plt.imread('480px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Display the image
plt.imshow(img)

# Hide the axes
plt.axis('off')
plt.show()

# '''''''''''  Pseudocolor Plot from Image Data ''#

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