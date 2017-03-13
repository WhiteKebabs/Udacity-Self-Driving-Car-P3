# Behavioral Cloner

## Outline

The purpose of this project is to use a driving simulator to collect driving data and feed the data into a Convolutional Neural Network to clone the behavior of the trainer. 

## Dependencies

In order to collect data, a simulator compatible with your operating system must be downloaded from below: 

<a href="https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58ae46bb_linux-sim/linux-sim.zip">Linux</a>
<a href="https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58ae4594_mac-sim.app/mac-sim.app.zip">macOS</a>
<a href="https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58ae4419_windows-sim/windows-sim.zip">Windows</a>

## Details of files in repo

### `model.py`
This script contains the code for the model. It currently uses the NVidia Self-Driving car model, which can be read about <a href="https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf">here</a>. The script will output the weights of the model current directory.


### `drive.py`
Contains the code necessary for testing the model created by model.py. The location of the file that contains the weights must be entered as an argument.

`python drive.py weights_location`
