# from keras.datasets import mnist
from PIL import Image
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
# from keras.models import Sequential
# from keras.layers import Conv2D, MaxPooling2D, Dropout, Dense, Flatten
# from keras.utils import np_utils

def preprocess_image(image_path):
    # Util function to open, resize and format pictures
    # into appropriate tensors.
    img = load_img(image_path)
    img = img_to_array(img)
    # convert to black and white
    return img[:,:,0] / 255

img_array = preprocess_image('magic_digits/1_0.png')
print(img_array.shape)
print(img_array)

# (X_train, y_train), (X_test, y_test) = mnist.load_data()
# print(X_train[0:10])
# from scipy import misc
# face = misc.face()
# # misc.imsave('magic_digits/0_0.png', face)
# img = misc.imread('magic_digits/0_0.png')
# face.tofile('magic_digits/0_0.png')
# img = np.fromfile('magic_digits/0_0.png')
# print(img.shape)
# print(img.dtype)
# import matplotlib.pyplot as plt
# plt.imshow(img, cmap=plt.cm.gray)
