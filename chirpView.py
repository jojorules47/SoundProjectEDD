import wave
from Equalizer import Equalizer
import matplotlib.pyplot as plt
import numpy as np

r = wave.open('mic.wav','r')
#print "Framelenght is ", r.getnframes()

buff = r.readframes(r.getnframes())
samps = np.fromstring(buff,dtype=np.int16)
r.close()
#f = np.fft.rfft(samps[::2])
#ff = np.zeroes(500000,dtype=np.complex)
#f[:10000]=0
#sig = np.fft.irfft(f)

#f = np.fft.rfft(samps)
size = 999
loops = len(samps)/size
f = np.zeros(500,dtype=np.complex)
for cnt in range(loops):
    f += np.fft.rfft(samps[cnt*size:cnt*size+size])
mag = np.abs(f)
ave = np.average(mag[100:300])*2
filt = np.clip(ave/mag,0,10)/10
twos = 2 * np.ones(500)
nfilt = twos - filt

r = wave.open('chirp.wav','r')
buff = r.readframes(r.getnframes())
samps = np.fromstring(buff,dtype=np.int16)
sample_rate_wave = 32000
nob_size = int(500.0 * sample_rate_wave / 32000)
nobs = np.ones(nob_size)
nobs[:500] = nfilt

eq = Equalizer()
eq.setNobs(nobs)
eq.makeResponse()
sig = eq.filterAll(samps)
w = wave.open('filt.wav','w')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(sample_rate_wave)
asig = np.array(sig,dtype=np.int16)
w.writeframes(asig.data)

plt.subplot(3,1,1)
plt.plot(mag/ave)
plt.subplot(3,1,2)
plt.plot(filt)
plt.subplot(3,1,3)
plt.plot(nfilt)
plt.show()
