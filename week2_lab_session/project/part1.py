# Load necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image and print the shape of the image

# Path to the image file
img_path = 'E:\\uob\Computer_Vision\Computer-Vision-and-Imaging-Lab\week2_lab_session\cs_building.png'

# Blank 1: Load the image using OpenCV's imread function
# Hint: Use cv2.imread() to read the image from the file.
# Complete the line to load the image
img = cv2.imread(img_path) ##cv2.imread()读取图像路径

# Blank 2: Print the shape of the image (height, width, channels)
# Hint: Use the .shape attribute of the image to print its dimensions.
# Complete the line to print the shape of the image
# Display the image using matplotlib
print(img.shape)
plt.imshow(img)
# %%
# Blank 3: Resize the image using OpenCV's resize function
# Hint: Use cv2.resize() to resize the image. The function takes the image and the desired dimensions (width, height) as inputs.
img_resized = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2)) # Complete the line to resize the image
#将图像缩放为原来的一半大小  cv2.resize()
# Display the resized image using matplotlib
plt.imshow(img_resized)
plt.title('Resized Image')
plt.show()
# %%
# Flip the image horizontally and vertically using NumPy

# Blank 4: Flip the image horizontally
# Hint: Use NumPy slicing to flip the image along the horizontal axis (flip across width).
horizontally_flipped_np = np.fliplr(img) # 水平翻转（沿着宽度轴反转） numpy.fliplr()左右变化Complete the line to flip the image horizontally

# Blank 5:  Flip the image vertically
# Hint: Use NumPy slicing to flip the image along the vertical axis (flip across height).
vertically_flipped_np = np.flipud(img) # 垂直翻转numpy.flipud()左右变化Complete the line to flip the image vertically

# Display the horizontally and vertically flipped images
plt.subplot(1, 2, 1)
plt.imshow(horizontally_flipped_np)
plt.title("Horizontally Flipped")

plt.subplot(1, 2, 2)
plt.imshow(vertically_flipped_np)
plt.title("Vertically Flipped")

plt.show()
# %%
# Besides using NumPy, OpenCV also allows you to flip images easily.

# Flip the image horizontally and vertically using OpenCV

# Blank 6: Flip the image horizontally
# Hint: Use cv2.flip() with the specific flip code to flip the image horizontally.
horizontally_flipped = cv2.flip(img,1) #使用cv2.flip实现翻转1是水平，0是竖直，-1是水平+竖直 Complete this line

# Blank 7: Flip the image vertically
# Hint: Use cv2.flip() with the specific flip code to flip the image vertically.
vertically_flipped = cv2.flip(img,0) # Complete this line

# Display the horizontally and vertically flipped images
plt.subplot(1, 2, 1)
plt.imshow(horizontally_flipped)
plt.subplot(1, 2, 2)
plt.imshow(vertically_flipped)
plt.show()
