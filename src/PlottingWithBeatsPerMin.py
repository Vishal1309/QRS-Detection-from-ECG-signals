import matplotlib.pyplot as plt
from PanTomkinsQRS import ecg, bp_filtered, der, sq, mwi_sig
from PlottingAfterDelay import delayed_ecg
from CalculatingHeartRate import pulse, Peak_Id
from changeSignal import signal_number
import numpy as np

plt.figure(figsize=(15,35)) 
plt.subplot(7,1,1)
plt.plot(ecg.iloc[100:2500,0], ecg.iloc[100:2500,1])
plt.title("Original Signal")

plt.subplot(7,1,2)
plt.plot(bp_filtered.iloc[100:2500,0], bp_filtered.iloc[100:2500,1])
plt.title("Output of Bandpass filter")

plt.subplot(7,1,3)
plt.plot(der.iloc[100:2500,0], der.iloc[100:2500,1])
plt.title("Output of Differentiator")

plt.subplot(7,1,4)
plt.plot(sq.iloc[100:2500,0], sq.iloc[100:2500,1])
plt.title("Output of squaring process")

plt.subplot(7,1,5)
plt.plot(mwi_sig.iloc[100:2500,0], mwi_sig.iloc[100:2500,1])
# plt.scatter(Peak_Id, peak_values, marker ="x", c="r")
plt.title("Results of moving window integration")

plt.subplot(7,1,6)
plt.plot(delayed_ecg.iloc[100:2500,0], delayed_ecg.iloc[100:2500,1])
plt.title("Original ECG signal delayed by total processing time")

plt.subplot(7,1,7)
plt.plot(pulse.iloc[100:2500,0], pulse.iloc[100:2500,1])
plt.title("Output Pulse Stream")

plt.savefig("QRS detection steps for signal " + str(signal_number),bbox_inches='tight')
# plt.show()

difference=[]
for n in range(len(Peak_Id)-1):
  difference.append(Peak_Id[n+1]- Peak_Id[n])
avg_RR=abs(np.mean(difference))

beats_per_min = (60 * 360 / (avg_RR)) 
print(beats_per_min)