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

[image1]: ./examples/placeholder.png "Model Visualization"
[image2]: ./examples/placeholder.png "Grayscaling"

---

###Model Architecture and Training Strategy

####1. An appropriate model architecture has been employed

| Layer         		    |     Description	        					            | 
|:---------------------:|:---------------------------------------------:| 
| Input         		    | 160x320x3 RGB image   							          | 
| Normalisation       	| 1x1 Stride, Same padding, Outputs 32x32x64	  |
| Max pooling	      	  | 2x2 Stride,  Outputs 16x16x64 				        |
| Local Response Norm	  | Depth radius 5, Bias 1.0, Alpha 1.0, Beta 0.5 |
| RELU					        |												                        |
| Convolution 5x5     	| 1x1 Stride, Same padding, Outputs 16x16x64 	  |
| Local Response Norm	  | Depth radius 5, Bias 1.0, Alpha 1.0, Beta 0.5 |
| Max pooling	      	  | 2x2 Stride, Outputs 8x8x64 	 			            |
| RELU					        |												                        |
| Fully connected		    | Input 4096, Outputs 384      									|
| Fully connected		    | Input 384, Outputs 192      									|
| Dropout               | 0.5 Keep probability                          |
| Fully connected		    | Input 192, Outputs 43       									|
| Softmax				        |         									                    |

####2. Attempts to reduce overfitting in the model

The model contains a dropout layer in order to reduce overfitting (model.py lines 66). 

The model was trained and validated on different data sets to ensure that the model was not overfitting (code line 77). The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

####3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 76).

####4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used a combination of center lane driving, recovering from the left and right sides of the road ... 

For details about how I created the training data, see the next section. 

###Model Architecture and Training Strategy

####1. Solution Design Approach

The overall strategy for deriving a model architecture was to ...

My first step was to use a convolution neural network model similar to the ... I thought this model might be appropriate because ...

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. I found that my first model had a low mean squared error on the training set but a high mean squared error on the validation set. This implied that the model was overfitting. 

To combat the overfitting, I modified the model so that ...

Then I ... 

The final step was to run the simulator to see how well the car was driving around track one. There were a few spots where the vehicle fell off the track... to improve the driving behavior in these cases, I ....

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.


####2. Creation of the Training Set & Training Process

To capture good driving behavior, I first recorded two laps on track one using center lane driving. Here is an example image of center lane driving:

![image1]

The biggest issue I encountered during the training process was getting the car to make sharp turns between striped lanes and lanes without lines. To overcome this, I recorded extra footages for these sharp turns so the model would learn to make the turns without having to overfit the model with additional epochs

As the course was circuit-like and initially I was only going counter-clockwise, most of the data was the car turning left. The easiest solution to this was to just drive clockwise around the circuit to give more variation to my dataset. Furthermore, I also augmented the data by flipping it horizontally. Below is a horizontally flipped version of the image above:

![image2]


After the collection process, I had 27842 number of data points. I then preprocessed this data by cropping the upper 70 pixels and lower 25 pixels of the images as they contained nothing significant for the model to extract infomation from.

Initially I tried training my model with 3 epochs, however as the models loss started to increase on the tird epoch, I decreased the number to 2, which achieved a loss of 0.01.
