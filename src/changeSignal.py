#@title Choose ECG Signal { form-width: "20%", display-mode: "both" }
signal_number = 9 #@param {type:"slider", min:0, max:9, step:1}
import wfdb
import numpy as np
import pandas as pd
np.set_printoptions(threshold=np.inf) # for printing the whole array

filename = f'/content/mit-bih-arrhythmia-database-1.0.0/{str(100 + signal_number)}'
record = wfdb.rdrecord(filename, sampfrom=180, sampto=4000,)    
annotation = wfdb.rdann(filename, 'atr', sampfrom=180, sampto=4000,shift_samps=True)

wfdb.plot_wfdb(record=record, annotation=annotation, time_units='seconds',figsize=(15,8))
# print(wfdb.rdsamp(filename, sampfrom=100, sampto=4000))

# .xws files are useless?
# .atr contains annotations - not zaroori for assignment
# .hea files contain info? patient details + file names + annotated comments + etc
# .dat file contains signal data