import wave
from Equalizer import Equalizer
import matplotlib.pyplot as plt
import numpy as np

r = wave.open('baby.wav','r')
#print "Framelenght is ", r.getnframes()

buff = r.readframes(r.getnframes())
samps = np.fromstring(buff,dtype=np.int16)
#f = np.fft.rfft(samps[::2])
#ff = np.zeroes(500000,dtype=np.complex)
#f[:10000]=0
#sig = np.fft.irfft(f)

eq = Equalizer()
nobs = np.ones(50000)
nobs[10000:20000] = 0.8
nobs[30000:40000] = 1.2
eq.setNobs(nobs)
eq.makeResponse()
sig = eq.filterAll(samps[::2])
w = wave.open('babyfilt.wav','w')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)
asig = np.array(sig,dtype=np.int16)
w.writeframes(asig.data)
#plt.plot(np.abs(f))
#plt.show()
