import matplotlib.pyplot as plt

from scipy.io import wavfile

samplerate,date = wavfile.read('1980s-Casio-Piano-C5.wav','r')
print(samplerate)