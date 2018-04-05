import numpy as np
import matplotlib.pyplot as plt

N = 2048
t = np.arange(N)

ph = 2.0*np.pi*t*t/float(N)

r = int(np.random.random()*512)
print "Random is ", r

chirp = np.zeros(4096, dtype="complex")
chirp[r:r+N] = np.sin(ph/4.0)
print "Length is ", len(chirp)
f = np.fft.rfft(chirp)


plt.subplot(2,1,1)
plt.plot(chirp)
plt.subplot(2,1,2)
plt.plot(20.0*np.log(np.abs(f)))
plt.show()
