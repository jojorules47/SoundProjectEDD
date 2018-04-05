import wave

r = wave.open('baby.wav','r')

import matplotlib.pyplot as plt
import numpy as np

buff = r.readframes(500000)
samps = np.fromstring(buff,dtype=np.int16)
f = np.fft.rfft(samps[::2])
#ff = np.zeroes(500000,dtype=np.complex)
f[:10000]=0
sig = np.fft.irfft(f)
w = wave.open('babyfilt.wav','w')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)
asig = np.array(sig,dtype=np.int16)
w.writeframes(asig.data)
plt.plot(np.abs(f))
plt.show()
