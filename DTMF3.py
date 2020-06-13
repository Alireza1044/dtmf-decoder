import sounddevice as sd
import soundfile as sf
from scipy.io import wavfile as wav
from DTMF1 import DTMF

if __name__ == '__main__':
    fs = 44100
    duration = 1  # seconds
    print('Listening...')
    while True:
        result = ''
        myrecording = sd.rec(duration * fs, samplerate=fs, channels=1, dtype='float64')
        sd.wait()
        sf.write('file.wav', myrecording, fs)
        rate, signal = wav.read('file.wav')
        result = DTMF(signal, rate)
        if (result != ''):
            print(result)
            print('Listening...')
