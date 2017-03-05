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

images, measurements = [], []
with open("./data/driving_log.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:

        steering = float(line[3])
        measurements += [steering, steering + 0.1, steering - 0.1]

        image_center = cv2.imread(line[0])
        image_left = cv2.imread(line[1])
        image_right = cv2.imread(line[2])
        images += [image_center, image_left, image_right]

augmented_images, augmented_measurements = [], []
for image, measurement in zip(images, measurements):
    augmented_images.append(image)
    augmented_measurements.append(measurement)
    augmented_images.append(cv2.flip(image,1))
    augmented_measurements.append(measurement*-1.0)

X_train = np.array(augmented_images)
y_train = np.array(augmented_measurements)

def compare_images(left_image, right_image):
    print(image.shape)
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
    f.tight_layout()
    ax1.imshow(left_image)
    ax1.set_title('Shape '+ str(left_image.shape),
                  fontsize=50)
    ax2.imshow(right_image)
    ax2.set_title('Shape '+ str(right_image.shape)
                  , fontsize=50)
    plt.show()

model = Sequential()
model.add(Lambda(lambda x: x/255.0 - 0.5, input_shape=(160, 320, 3)))
model.add(Cropping2D(cropping=((70, 25), (1, 1))))

# Display cropping before and after
#cropping_output = K.function([model.layers[1].input], [model.layers[1].output])
#cropped_image = cropping_output([image[None,...]])[0]
#compare_images(image, cropped_image.reshape(cropped_image.shape[1:]))

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
