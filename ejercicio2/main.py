import librosa
import matplotlib.pyplot as plt
import sounddevice as sd


# Leer archivo de audio
audio, fs = librosa.load('audio.wav', sr=None)

# Play the audio
sd.play(audio, samplerate=fs)

# Wait until the audio finishes playing
sd.wait()

