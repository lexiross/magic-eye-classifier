from PIL import Image
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Dense, Flatten
from keras.utils import np_utils

NUM_DIGITS = 10
SAMPLES_PER_DIGIT = 100
TRAINING_PROPORTION = 0.8
IMG_WIDTH = 400
IMG_HEIGHT = 400

def preprocess_image(image_path):
    img = load_img(image_path)
    img = img_to_array(img)
    # convert to black and white
    return img[:,:,0] / 255.

def load_data():
    count = 0
    num_samples = NUM_DIGITS * SAMPLES_PER_DIGIT
    training_count = int(num_samples * TRAINING_PROPORTION)
    X_train = np.zeros([training_count, IMG_WIDTH, IMG_HEIGHT])
    y_train = np.zeros(training_count)
    X_test = np.zeros([num_samples - training_count, IMG_WIDTH, IMG_HEIGHT])
    y_test = np.zeros(num_samples - training_count)
    for i in range(SAMPLES_PER_DIGIT):
        for j in range(NUM_DIGITS):
            filename = 'magic_digits/' + str(j) + '_' + str(i) + '.png'
            img_array = preprocess_image(filename)
            if (count >= training_count):
                idx = count - training_count
                X_test[idx] = img_array
                y_test[idx] = j
            else:
                X_train[count] = img_array
                y_train[count] = j

            count += 1
    return (X_train, y_train), (X_test, y_test)



(X_train, y_train), (X_test, y_test) = load_data()

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

# one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]

# build model

def train_mnn(X_train, y_train, X_test, y_test):
    model = Sequential()

    model.add(Flatten(input_shape=(IMG_WIDTH,IMG_HEIGHT)))
    model.add(Dropout(0.5))
    model.add(Dense(30, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(30, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train, validation_data=(X_test, y_test))

def train_cnn(X_train, y_train, X_test, y_test):
    # reshape input data
    X_train = X_train.reshape(X_train.shape[0], IMG_WIDTH, IMG_HEIGHT, 1)
    X_test = X_test.reshape(X_test.shape[0], IMG_WIDTH, IMG_HEIGHT, 1)

    model = Sequential()
    model.add(Conv2D(8, (5, 5), input_shape=(IMG_WIDTH, IMG_HEIGHT,1), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(32, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train, validation_data=(X_test, y_test))

# train_cnn(X_train, y_train, X_test, y_test)
train_mnn(X_train, y_train, X_test, y_test)
