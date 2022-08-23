from PanTomkinsQRS import mwi_sig, output_signal
class Beat_Detector():
    def search_back(self, isQRS, SPKI, PEAKI, THRESHOLD_I2):
      if(PEAKI > THRESHOLD_I2):
          SPKI = 0.25*PEAKI + 0.75 * SPKI
          isQRS = True

    def Pulse_gen(self,signal,peaks):
        pulse_stream = signal.copy()

        for i in signal.index:
            if(i not in peaks):
                pulse_stream.iloc[i,1] = 0
            else:
                pulse_stream.iloc[i,1] = 1
        return pulse_stream

    def Heartbeat_thresholding(self,signal):
        min_RR = 40
        max_RR = 400
        SPKI = 0 # initializing the Signal and noise peaks to 0
        NPKI = 0
        peaks=[]
        THRESHOLD_I1 = SPKI # initializing the threshold to 0
        THRESHOLD_I2 = SPKI
        searchback = False
        en_searchback = 0
        prev = 0
        i=2
        while i<len(signal)-2:
            if (i-prev > max_RR and i-en_searchback > max_RR):
                en_searchback = i
                searchback = True
                i = prev+2
                continue
            if (searchback == True and i==en_searchback):
                searchback = False
                continue
            PEAKI = signal.iloc[i,1]
            if (PEAKI < signal.iloc[i-1,1] or PEAKI <= signal.iloc[i+1,1]):
                i+=1
                continue
            
            isQRS = False

            if (searchback == True):
                self.search_back(isQRS, SPKI, PEAKI, THRESHOLD_I2)
            elif (THRESHOLD_I1 < PEAKI):
                SPKI = 0.875*SPKI + 0.125*PEAKI
                isQRS = True

            if isQRS == False:
                NPKI = 0.125*PEAKI + 0.875*NPKI
            else:
                if (prev == 0 or i - prev >= min_RR):
                    peaks.append(i)
                elif (signal.iloc[prev,1] < PEAKI):
                    peaks[-1] = i
                prev = i
            
            THRESHOLD_I1 = 0.25*SPKI + 0.75*NPKI # from the reference equations to compute thresholds
            THRESHOLD_I2 = 0.5*THRESHOLD_I1
            i+=1
        return peaks

    def solve(self,signal):
        f1 = self.Heartbeat_thresholding(signal)
        pulse = self.Pulse_gen(signal,f1)
        return f1,pulse

detector = Beat_Detector()
Peak_Id, pulse = detector.solve(output_signal)
peak_values = []
for i in Peak_Id:
  peak_values.append(mwi_sig.iloc[i, 1])
print(Peak_Id)
