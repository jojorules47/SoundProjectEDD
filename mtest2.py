import alsaaudio,time,audioop
import matplotlib.pyplot as plt
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
inp.setchannels(1)
inp.setrate(32000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)

stuff = 0
thing = []
test = True
mtest = open("testfile.txt","w")
for i in range(0,5000):
    thing.append(0)

while test == True:
    l,data = inp.read()
    if l:
        thing[stuff] = audioop.max(data,2)
        print(audioop.max(data,2))
    time.sleep(.001)
    stuff += 1
    if stuff >= 5000:
        test = False
        mtest.write(str(thing))
        mtest.close()
        plt.plot(stuff,thing)
        plt.show()
