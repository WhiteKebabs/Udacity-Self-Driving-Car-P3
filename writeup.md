#**Behavioral Cloning** 

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./figures/correct.jpg "Sample input"
[image2]: ./figures/flipped.jpg "Augmented input"

---

###Model Architecture and Training Strategy

####1. An appropriate model architecture has been employed

| Layer         		    |     Description	        					            | 
|:---------------------:|:---------------------------------------------:| 
| Input         		    | 160x320x3 RGB image   							          | 
| Normalisation       	|                                           	  |
| Cropping   	      	  | Outputs 65x328x3              				        |
| Convolution 5x5   	  | Outputs 31x157x24                             |
| Dropout             	| 0.5 Keep probability	                        |
| Convolution 5x5   	  | Outputs 14x77x36                              |
| Convolution 5x5       |	Outputs 5x37x48				                        |
| Convolution 3x3		    | Outputs 3x35x64             									|
| Convolution 3x3		    | Outputs 1x33x64             									|
| Fully Connected Layer | Outputs 100 							                    |
| Fully Connected Layer | Outputs 50 								                    |
| Fully Connected Layer | Outputs 10       					                    |
| Fully Connected Layer | Outputs 1                                     |

####2. Attempts to reduce overfitting in the model

The model contains a dropout layer in order to reduce overfitting (model.py lines 66). 

The model was trained and validated on different data sets to ensure that the model was not overfitting (code line 77). The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

####3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 76).

###Model Architecture and Training Strategy

####1. Solution Design Approach

The model used to train the autonomous car is very similar to the NVidia architecture shown in the lecture videos. The only modification made to the model was a dropout later between the first and second convolution layers to prevent overfitting. I decided to use specifically this architecture as it is already being used on the road and is far more complex than any of the previous models I have used in this course.

####2. Creation of the Training Set & Training Process

To capture good driving behavior, I first recorded two laps on track one using center lane driving. Here is an example image of center lane driving:

![image1]

The biggest issue I encountered during the training process was getting the car to make sharp turns between striped lanes and lanes without lines. To overcome this, I recorded extra footages for these sharp turns so the model would learn to make the turns without having to overfit the model with additional epochs

As the course was circuit-like and initially I was only going counter-clockwise, most of the data was the car turning left. The easiest solution to this was to just drive clockwise around the circuit to give more variation to my dataset. Furthermore, I also augmented the data by flipping it horizontally. Below is a horizontally flipped version of the image above:

![image2]


After the collection process, I had 27842 number of data points. I then preprocessed this data by cropping the upper 70 pixels and lower 25 pixels of the images as they contained nothing significant for the model to extract infomation from.

Initially I tried training my model with 3 epochs, however as the models loss started to increase on the tird epoch, I decreased the number to 2, which achieved a loss of 0.01.
