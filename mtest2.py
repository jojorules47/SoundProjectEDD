import alsaaudio,time,audioop
import matplotlib.pyplot as plt
import numpy as np
import wave

card = "hw:2,0"
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK,card)
inp.setchannels(1)
inp.setrate(32000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)

stuff = 0
buff = np.array([])
test = True
while test == True:
    l,data = inp.read()
    if l:
        numpydata = np.fromstring(data,dtype=np.int16)
        buff = np.concatenate((buff,numpydata))
    stuff += 1
    if len(buff) >= 160000:
        test = False
        
        w = wave.open('mic.wav','w')
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(44100)
        asig = np.ndarray(buff,dtype=np.int16)
        w.writeframes(asig)

#        plt.plot(buff)
#        plt.show()
