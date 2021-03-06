import csv
import cv2
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Dropout
from keras.layers.convolutional import Convolution2D, Cropping2D
from keras.layers.pooling import MaxPooling2D
from keras import backend as K
import matplotlib.pyplot as plt

# Open the CSV that has the camera images and steering angles
images, measurements = [], []
with open("./data/driving_log.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:

        # Extract steering angle for straight view
        # Correct the steering angle for left and right cameras
        steering = float(line[3])
        measurements += [steering, steering + 0.1, steering - 0.1]

        # Extract the three camera angles
        image_center = cv2.imread(line[0])
        image_left = cv2.imread(line[1])
        image_right = cv2.imread(line[2])
        images += [image_center, image_left, image_right]

# Create augmented images from the dataset
augmented_images, augmented_measurements = [], []
for image, measurement in zip(images, measurements):

    # Flip the image horizontally
    augmented_images.append(image)
    augmented_images.append(cv2.flip(image,1))

    # Negate the steering angle
    augmented_measurements.append(measurement)
    augmented_measurements.append(measurement*-1.0)

# Convert the training dataset and labels to Numpy arrays
X_train = np.array(augmented_images)
y_train = np.array(augmented_measurements)


# Model Implementation
model = Sequential()
model.add(Lambda(lambda x: x/255.0 - 0.5, input_shape=(160, 320, 3)))
model.add(Cropping2D(cropping=((70, 25), (1, 1))))
model.add(Convolution2D(24,5,5, subsample=(2,2), activation="relu"))
model.add(Dropout(0.5))
model.add(Convolution2D(36,5,5, subsample=(2,2), activation="relu"))
model.add(Convolution2D(48,5,5, subsample=(2,2), activation="relu"))
model.add(Convolution2D(64,3,3, activation="relu"))
model.add(Convolution2D(64,3,3, activation="relu"))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=2)

model.save('model.h5')
