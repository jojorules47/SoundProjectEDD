import numpy as np
import matplotlib.pyplot as plt
from Equalizer import Equalizer

N = 16
K = 4

a = np.random.rand(N)
b = np.random.rand(K)
c = np.zeros(N)

for n in range(N-K):
#    for k in range(K):
#        idx = (n + k) % N
        nidx = (n + K - 1) % N
        c[nidx] = a[n] * b[3] + a[n+1] * b[2] + a[n+2] * b[1] + a[n+3] * b[0]
#        c[nidx] += a[idx]*b[K-k-1]

f = np.fft.irfft(np.fft.rfft(a,N)*np.fft.rfft(b,N))

eq = Equalizer()
nobs = np.ones(500)
nobs[:100] = 0
eq.setNobs(nobs)
eq.makeResponse()
im = eq.getImpulse()

plt.subplot(2,1,1)
plt.plot(im)
plt.subplot(2,1,2)
plt.plot(f)
plt.show()
