import sounddevice as sd

fs=44100
sd.default.samplerate = fs
sd.default.channels = 2
duration = 3  # seconds
aki = sd.rec(int(duration * fs),dtype='float64')

sd.wait()
#asi = sd.playrec(aki)
#sd.wait()

print(aki)
sd.play(aki)
#print('played aki')
#sd.play(asi)