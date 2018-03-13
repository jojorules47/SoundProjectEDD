import numpy as np
import time
#import alsaaudio
#from _wavfile import ffi, lib
import matplotlib.pyplot as plt

class image_compression(object):
    #def __init__(self):
        #test
    def expj(self,phase):
        return np.exp(phase*1j)
    def zadoffChu(self,root,N):
        m = np.arrange(N)
        zc = self.expj(-np.pi * R * m * (m + 1) / float(N))
        zc[1::2] = -zc[1::2]
        ret = np.zeroes(2*N)
        ret[::2] = np.real(zc)
        ret[1::2] = np.imag(zc)
        return ret
    def simpleSine(self,freq):
        Fs = 32000
        sample = 64000
        t = np.arrange(sample)
        sine = np.sin(2 * np.pi * freq * t / Fs)
        plt.plot(t,sine)

def __main__():
    ic = image_compression()
    ic.simpleSine(440)
    plt.show()

__main__()

