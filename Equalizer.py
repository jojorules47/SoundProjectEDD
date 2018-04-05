import numpy as np

class Equalizer(object):
    def __init__(self):
        self.nobs = None
        self.N = None
        self.impulse = None
        self.response = None

    def setNobs(self,nobs):
        self.nobs = nobs
        self.N = len(self.nobs)*4

    def makeResponse(self):
        t = np.arange(self.N/4)
        exp = np.exp(-1j*np.pi*t/2.0)
        fresp = self.nobs*exp
        imp = np.fft.irfft(fresp)
        self.response = np.fft.rfft(imp, self.N)
        self.impulse = np.fft.irfft(self.response, self.N)

    def getImpulse(self):
        return self.impulse

    def getResponse(self):
        return self.response

    def doFilter(self,wave):
        if len(wave) != self.N:
            raise AssertionError('imput must be ' + str(self.N) + ' elements not ' + str(len(wave)))
        freqs = np.fft.rfft(wave)
        chan = freqs*self.response
        ret = np.fft.irfft(chan)
        return ret[self.N/2:]

    def filterAll(self,song):
        loops = len(song)/(self.N/2) + 1
        ret = np.zeros(loops*self.N/2)
        for cnt in range(loops - 2):
            idx = cnt*self.N/2
            wave = song[idx:idx+self.N]
            channel = self.doFilter(wave)
            ret[idx:idx + self.N/2] = channel
        # do last loop
        idx = (loops-1)*self.N/2
        wave = np.zeros(self.N)
        data = song[idx:]
        wave[:len(data)] = data
        channel = self.doFilter(wave)
        ret[idx:idx + self.N/2] = channel
        return ret
