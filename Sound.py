import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft,fftfreq

import sys

def printCmd(str):
    h = (32*'-')+'\n'
    print(h+str+'\n'+h)

class Sound:
    def __init__(self,**kwargs):
        if (kwargs['path'] == ''):
            raise AttributeError('please insert a path')
        else:
            self.path = kwargs['path']

        try:
            self.name = kwargs['name']
        except:
            self.name = self.path

        self.data = []
        self.samplerate = 0
        self.fft = []
        self.frame = 0
        printCmd('\''+self.name + '\' created.')

    def readWav(self):
        samplerate,data = wavfile.read(self.path,'r')
        printCmd('sample rate: '+samplerate)
        self.data = data
        self.samplerate = samplerate
        return self.data

    def initFFT(self):
        self.fft = fft(self.data)

    def getFFT(self):
        return self.fft

    def draw(self):
        plt.figure(self.name)
        plt.plot(self.data)
        plt.grid(True)
        plt.show()

    def drawFFT(self):
        plt.figure(self.name + ' FFT')
        plt.plot(self.fft)
        plt.xlim([10, self.samplerate / 2])
        plt.xscale('log')
        plt.grid(True)
        plt.xlabel('Frequency (Hz)')
        plt.show()

    def drawAll(self):
        plt.figure(self.name)
        plt.plot(self.data)
        plt.grid(True)
        plt.figure(self.name + ' FFT')
        plt.plot(self.fft)
        plt.xlim([10, self.samplerate / 2])
        plt.xscale('log')
        plt.grid(True)
        plt.xlabel('Frequency (Hz)')
        plt.show()

    def __str__(self):
        return self.data