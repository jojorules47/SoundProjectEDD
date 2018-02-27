import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

#info=audio.get_host_api_info_by_index(0)
#numdevices = info.get('deviceCount')
#for i in range(0,numdevices):
#    if(audio.get_device_info_by_host_api_device_index(0,i).get('maxInputChannels')) > 0:
#        print('Input Device id ', i, ' - ', audio.get_device_info_by_host_api_device_index(0,i).get('name')


stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
print("recording...")
frames=[]
for i in range(0,int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
#import alsaaudio, time, audioop

#inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudia.PCM_NONBLOCK)

#inp.setchannels(1)
#inp.setrate(8000)
#inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

#inp.setperiodsize(160)

#while True:
#    l,data = inp.read()
#    if l:
#        print audioop.max(data,2)
#    time.sleep(.001)
#    frames.append(data)
print("finished recording")



stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME,'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
