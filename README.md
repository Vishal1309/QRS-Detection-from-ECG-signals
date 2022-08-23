# Assignment 2

## My Understanding of the Algorithm

### Introduction
The Pan-Tompkins algorithm detects QRS complexes (peaks in ecg) in electrocardiograph (ECG) signals in real time. There is a lot of noise in real-time ECG readings that has to be filtered away. The *QRS complex* is a feature of an ECG signal that is used to calculate heart rate. The Pan-Tompkins method proposes applying a series of filters, namely - 1)Bandpasss Filter, 2) Derivative, 3) Squaring, 4) Moving Window Integration, to an input ECG signal in order to produce an output with clearly apparent QRS complexes (clear peaks).

### Band Pass Filter
The band pass filter allows only a certain pass-band frequency of 5-12 Hz. Since the measured ECG signals have high frequency noise in them, we pass them through a bandpass filter to smooth the signals. This filter is implemented by passing the input ECG signal through a high pass filter and passing the output signal of this filter into a low pass filter. This output of this is essentially the band pass filtered signal. (these filters are implemented using the difference equations for the high and low pass filters.) 

### Derivative
Once we are done with removing the noise from the input signal, we now have to take its derivative for beginning the processing of the signal. We compute the derivative since the purpose of the algorithm is to determine the peaks which requires a derivative signal. So, for implementing the derivative function, we use a difference equation with the 5 point derivative.

### Squaring
For squaring, the implementation is as simple as squaring the signal at every point.  This essentially helps us make the peaks in the graph more prominent for generating a more consistent QRS complex. The negative values of slopes are squared. This essentially amplifies the values of peak value components in the signal. This freqency amplification also decreases the odds of detecting false positives from T waves.

### Moving Window Integration
In the moving window integration technique, the size of the window is chosen by the means of observation that helps amplify the QRS complex. We are using 30 samples for the moving window integration as mentioned in the paper. This function provides information about both the width and slope of the complex. This width of the output informs us about the time duration of the QRS signal.

### Delay
As mentioned in the reference paper, each step of the algorithm takes some time for processing. This time breakdown for the individual functions goes as follows: 

#### Delay: 
* 16 samples for High Pass Filter
* 6 samples for Low Pass Filter 
* 2 samples for Derivative

So, the total delay = 24 samples.

### Moving Window Integrated Signal
The output signal obtained after passing it through all the processing functions has prominent peaks as well as some small peaks beside them. These correspond to the T wave and are supposed to be eliminated to prevent the detection of false positives.

### Thresholding to determine valid QRS peaks
Now that we have obtained an output signal, we need to find the valid peaks from the availabe peaks by adaptive thresholding. We have established that two peaks need to be at least 200 ms apart and at most 2000 ms apart and the change in slope at a point is characterised as a peak. Once we get a value which falls within the given conditions, we check for if it lies within the threshold value to differentiate between signal and noise peaks.

### HeartRate
For calculating the heartrate, i.e, number of beats per minute, we first find the average RR, i.e, the average gap between two peaks of Heartbeat_thresholdings. With a sampling rate of 360 samples/s. A simple cross-multiplication gives us -> (360 (samples/ sec) * (60 sec)) / (Average gap between two heatbeats)) beats in a minute, i.e, the heartrate.

### Assumptions
-> We initialize NPKI (noise peaks), SPKI (signal peaks) and thresholds all to 0 at the beginning.

### Eliminating T waves
The adaptive thresholding and squaring eleminates small T waves preventing false positives.

### Searchback
Peaks need to have a minimum gap of 200 ms. If we cannot find the next peak within 2000ms while implementing first threshold, we use the second threshold while searchback. In this case we use a different threshold equation while updating the threshold values.


## Results

You will have to show results for each signal 0-9 for the various filters over them. Do consider properly labeling your plots. Also report ***heart rate*** for each ecg signal.

Note: you can stick pictures, code is not required for this section
![picture](https://i.ibb.co/3C6r4qP/results-eg.png) 



## Plots

**FOR ALL THE PLOTS BELOW, THE X-AXIS is the Time axis (ms) and the Y-AXIS is the SIGNAL VALUE**

**For signal 0 (Heart Rate = 82 BPM):**
![picture](https://drive.google.com/uc?export=view&id=1fesJEMeZJ9SYjyIhwVC-cGvbSy6Ycvb2)


**For signal 1 (Heart Rate = 74 BPM):**
![picture](https://drive.google.com/uc?export=view&id=1vv3m718X84MluClyQSI2w8Wf7df3Nto6)

**For signal 2 (Heart Rate = 79 BPM):**
![picture](https://drive.google.com/uc?export=view&id=12BElJ5XciKaqnvsgoZzhEE2Fs2ed3uCL)

**For signal 3 (Heart Rate = 79 BPM):**
![picture](https://drive.google.com/uc?export=view&id=1NZdW-fl86q3TG1Nh5s_rD_03CUaZq-eq)


**For signal 4 (Heart Rate = 77 BPM):**
![picture](https://drive.google.com/uc?export=view&id=1zaizTRVNKPqeQNQbd5iRPBsrLHl5C2BP)

**For signal 5 (Heart Rate = 83 BPM):**
![picture](https://drive.google.com/uc?export=view&id=1HMrt8rfQJTPybw_aHoevzt_SbAS8rop-)

**For signal 6 (Heart Rate = 68 BPM):**
![picture](https://drive.google.com/uc?export=view&id=1wJKLi0BIKdTP8PanY3R0sTG3oGTY3LCG)

**For signal 7 (Heart Rate = 92 BPM):**
![picture](https://drive.google.com/uc?export=view&id=13ENF7lzs_qh0MtBGE1JicKJ2H4y9O6xh)

**For signal 8 (Heart Rate = 46 BPM):**
![picture](https://drive.google.com/uc?export=view&id=1a4le_grkWBWFzsWkRHftcuTGGF0J_Gku)

**For signal 9 (Heart Rate = 100 BPM):**
![picture](https://drive.google.com/uc?export=view&id=1zHNo6vh2nNVz4Gus_KcN7i7gSkUKvB6p)


## Conclusion

The algorithm detects QRS with high reliability and in real time. The bandpass filter smoothens the noise signal and allows for lower threshold values for peak detection with high sensitivity. The searchback technique detects missed peaks to make the algorithm more robust and reliable. the threshold values are also updated in real time. This gives a high performance on various types of signals with diverse signal characteristics and ORS morphologies.
