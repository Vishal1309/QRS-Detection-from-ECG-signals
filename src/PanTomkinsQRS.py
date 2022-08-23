import pandas as pd
import numpy as np
from changeSignal import record
# import pandas as pd
# import matplotlib.pyplot as plt
class Pan_Tompkins_QRS():
  
  def band_pass_filter(self,signal):
    '''
    Band Pass Filter
    :param signal: input signal
    :return: prcoessed signal

    Methodology/Explaination (min 2-3 lines):
    [TODO] 
    This filters the signal to give the output signal with frequencies in a given range.
    For creating the band-pass filter, I first passed the signal through the high pass filter and then passed the signal obtained from that through the low pass filter. 
    This esentially gives me the bandpass fitlered signal --> band_pass =  low_pass(high_pass(signal))
    For implementing the high and low pass filters, I used the difference equations from the reference paper.
    '''
    # create a band pass filter that allows frequencies in the range of 5 - 12 Hz

    # Creating a high-pass filter first-->
    hpf_signal = signal.copy()
	
    for n in signal.index:
      # difference equation of the high-pass filter
      if(n>= 32):
        hpf_signal.iloc[n, 1] = (32*signal.iloc[n - 16, 1] - ( hpf_signal.iloc[n - 1, 1] + signal.iloc[n, 1] - signal.iloc[n - 32, 1]))
        hpf = hpf_signal.copy()

    # now implementing low-pass filter on the signal obtained after passing it through high-pass filter
    lpf_signal = hpf.copy()
    
    for n in hpf.index:
      if(n < 12):
        continue
      # difference equation of the low-pass filter
      lpf_signal.iloc[n, 1] = (2*lpf_signal.iloc[n - 1, 1] - lpf_signal.iloc[n - 2, 1] + hpf.iloc[n, 1] - 2*hpf.iloc[n - 6, 1] + hpf.iloc[n - 12, 1])  
      # this lpf_signal is the band-filtered signal itself since I have passed the same signal through both high and low pass filters now.
      bpf = lpf_signal.copy()
    return bpf
    
  
  def derivative(self,signal):
    '''
    Derivative Filter 
    :param signal: input signal
    :return: prcoessed signal

    Methodology/Explaination (min 2-3 lines):
    [TODO] 
    Here, I used the difference equation for derivative in the paper for obtaining the output signal after getting taking the derivative of the band-pass filtered signal passed in it.
    I used the five-point derivate to prvide QRS-complex slope information 
    '''
    # derivative of the signal --> d_signal
    d_signal = signal.copy()

    for n in signal.index:
      if(n < 4):
        continue
      # difference equation of the derivative
      if(n+2 < len(signal)): d_signal.iloc[n, 1] = (1 / 8) * ( -signal.iloc[n-2,1] - 2 * signal.iloc[n-1, 1] + 2 * signal.iloc[n+1, 1] + signal.iloc[n+2, 1] )
    return d_signal

  def squaring(self,signal):
    '''
    Squaring the Signal
    :param signal: input signal
    :return: prcoessed signal

    Methodology/Explaination (min 2-3 lines):
    [TODO] 
    Here, I pass the derivatve signal to the squaring funciton for performing point by point squaring.
    This makes all data points positive and performs nonlinear amplification of the derivative's output, highlighting the higher frequencies.
    '''
    # squared signal --> sq_signal
    sq_signal = signal.copy()

    for n in signal.index:
      sq_signal.iloc[n,1] = ( signal.iloc[n,1] )**2
    return sq_signal

  def moving_window_integration(self,signal):
    '''
    Moving Window Integrator
    :param signal: input signal
    :return: prcoessed signal

    Methodology/Explaination (min 2-3 lines):
    [TODO] 
    In addition to the slope of the R wave, we also require information about the waveform feature. So, we use moving window integration with the window size of 30.
    using the difference equation in the reference which takes window integrals at each step and returns the overall integral.
    '''
    # Window Size --> w_s
    w_s = 30 

    mwi = signal.copy()
    for i in range(w_s-1,len(signal)): # from 29 -> n integrating for all the points from where we can get the window
        sigma_window = 0
        for j in range(1,w_s+1): # integrating the window
            sigma_window+=signal.iloc[i-(w_s-j),1]
        mwi.iloc[i,1] = sigma_window/w_s

    return mwi

  def solve(self,signal):
    '''
    Solver, Combines all the above functions
    :param signal: input signal
    :return: prcoessed signal

    Methodology/Explaination (min 2-3 lines):
    [TODO] 
    passing the original signal through the bandpass filter to get the bandpass filtered signal. 
    Then passing this filtered signal through a differentiator to obtain a differentiated signal.
    We then square the resultant signal and pass it through the movind window integrator so that we can obtain the waveform feature information.
    '''
    #[TODO]
    # 1. bandpass
    # 2. differentiate
    # 3. square
    # 4. integrate
    bpf_sig = self.band_pass_filter(signal)
    der_sig = self.derivative(bpf_sig)
    sq_sig = self.squaring(der_sig)
    mwi_sig = self.moving_window_integration(sq_sig)
    l = [bpf_sig, der_sig, sq_sig, mwi_sig]
    return mwi_sig


QRS_detector = Pan_Tompkins_QRS()


ecg = pd.DataFrame(np.array([list(range(len(record.adc()))),record.adc()[:,0]]).T,columns=['TimeStamp','ecg'])
output_signal = QRS_detector.solve(ecg)

original = ecg.copy(); #original signal
bp_filtered = QRS_detector.band_pass_filter(original) # bandpass filtered signal
der = QRS_detector.derivative(bp_filtered) # derivative signal
sq = QRS_detector.squaring(der) # squared signal
mwi_sig = QRS_detector.moving_window_integration(sq) # moving window integrated signal