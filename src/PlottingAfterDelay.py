from PanTomkinsQRS import ecg, original, bp_filtered, der, sq, mwi_sig

# implementing delay of 16 for high-pass, 6 for low-pass, 2 for derivative.
delay = 24
delayed_ecg = ecg.copy()
for i in range(len(delayed_ecg)-1, -1, -1):
  if i >= delay:
    delayed_ecg.iloc[i, 1] = ecg.iloc[i-delay, 1]
  else:
    delayed_ecg.iloc[i, 1] = ecg.iloc[delay, 1]


import matplotlib.pyplot as plt

plt.figure(figsize=(15,35))
plt.subplot(5, 1, 1)
plt.plot(original.iloc[100:2500,0], original.iloc[100:2500,1])
plt.title("Original Signal")

plt.subplot(5, 1, 2)
plt.plot(bp_filtered.iloc[100:2500,0], bp_filtered.iloc[100:2500,1])
plt.title("After applying BandPass Filter")

plt.subplot(5, 1, 3)
plt.plot(der.iloc[100:2500,0], der.iloc[100:2500,1])
plt.title("After taking derivative")

plt.subplot(5, 1, 4)
plt.plot(sq.iloc[100:2500,0], sq.iloc[100:2500,1])
plt.title("After Squaring")

plt.subplot(5, 1, 5)
plt.plot(mwi_sig.iloc[100:2500,0], mwi_sig.iloc[100:2500,1])
plt.title("After Moving Window Integration")
plt.show()