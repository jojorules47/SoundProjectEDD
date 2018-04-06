import numpy as np
import matplotlib.pyplot as plt
import wave

N = 262144*2
t = np.arange(N)

ph = 2.0*np.pi*t*t/float(N)

chirp = 16000*np.sin(ph/4.0)
f = np.fft.rfft(chirp)

w = wave.open('chirp.wav','w')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(32000)
asig = np.array(chirp,dtype=np.int16)
w.writeframes(asig.data)
w.close()


plt.subplot(2,1,1)
plt.plot(chirp)
plt.subplot(2,1,2)
plt.plot(20.0*np.log(np.abs(f)))
plt.show()
