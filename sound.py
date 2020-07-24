import matplotlib.pyplot as plt
import numpy as np
from IPython.lib.display import Audio
from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq
import logging
from tempfile import mkdtemp
import os.path as path
import sys

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w',
                    format='%(levelname)s - %(name)s: %(message)s')

class Hn:
    def __init__(self, **kwargs):
        self.data = []
        self.name = 'H[n]'
        self.path = None
        self.points = [[], []]
        if kwargs['path'] != '':
            self.path = kwargs['path']
            file = open(self.path, 'r')
            for line in file:
                self.data += [float(line)]
        elif kwargs['data']:
            self.data = kwargs['data']
        elif kwargs['path'] != '' and kwargs['data']:
            logging.debug('please insert a path or array of data')
            raise AttributeError('please insert a path or array of data')
        else:
            logging.debug('please insert a path or array of data')
            raise AttributeError('please insert a path or array of data')
        logging.info('Hn = {}'.format(str(self.data)))

        for i in range(len(self.data)):
            self.points[0] += [i]
            self.points[1] += [self.data[i]]

    def draw(self):
        plt.title(self.name)
        plt.plot(self.points[0], self.points[1])
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.savefig('{}'.format(self.name))
        plt.grid(True)
        plt.show()

    def draw_phase(self):
        plt.title(self.name + 'Phase spectrum')
        plt.phase_spectrum(self.points[1])
        plt.savefig('{} Phase spectrum'.format(self.name))
        plt.grid(True)
        plt.show()

    def __str__(self):
        return self.data


class Noise:
    def __init__(self, **kwargs):
        self.data = []
        self.sample_rate = 0
        self.fft = []
        self.frame = 0
        self.path = None

        if kwargs['path']:
            self.path = kwargs['path']
            self.parse_wav()
        elif kwargs['data'] is not None:
            self.data = kwargs['data']
            self.sample_rate = 32000
            logging.info('noise data = {}'.format(self.data))
        elif kwargs['path'] != '' and kwargs['data']:
            logging.debug('please insert a path or array of data')
            raise AttributeError('please insert a path or array of data')
        else:
            logging.debug('please insert a path or array of data')
            raise AttributeError('please insert a path or array of data')

        try:
            self.name = kwargs['name']
        except:
            self.name = 'Unknown' if self.path is None else self.path

        logging.info('{} noise created.'.format(self.name))

    def parse_wav(self):
        sample_rate, data = wavfile.read(self.path, 'r')
        self.data = data
        self.sample_rate = sample_rate
        logging.info('noise sample rate = {}'.format(self.sample_rate))
        logging.info('noise data = {}'.format(self.data))
        return self.data

    def init_fft(self):
        self.fft = fft(self.data)

    def get_fft(self):
        self.init_fft()
        return self.fft

    def get_energy(self):
        return np.sum((np.abs(self.data) ** 2)) / len(self.data)

    def get_duration(self):
        return len(self.data) / float(self.sample_rate)

    def get_slice(self, slc):
        length = len(self.data)
        mul = (slc / self.get_duration()) * length
        index = int(mul)
        return Noise(name='{}s of {}'.format(slc, self.name), data=self.data[0:index], path='')

    def get_max(self):
        return np.amax(self.data)

    def when_max(self):
        length = len(self.data)
        index = np.where(self.data == self.get_max())
        when = ((index[0] * self.get_duration()) / length)[0]
        logging.info('{} at {}s is max'.format(self.name, when))
        return when

    def shift_right(self, slc):
        if slc < 0:
            return self.shift_left(abs(slc))
        amount = int(slc * self.sample_rate)
        filename = path.join(mkdtemp(), 'newfile.dat')
        fpath = np.memmap(filename, dtype='float64', mode='w+', shape=len(self.data))
        fpath[amount:] = self.data[:-amount]
        logging.info('{} {} shifted right'.format(self.name, amount))
        return Noise(name='{} time shifted right {}'.format(amount, self.name),
                     data=fpath, path='')

    def shift_left(self, slc):
        if slc < 0:
            return self.shift_right(abs(slc))
        amount = int(slc * self.sample_rate)
        filename = path.join(mkdtemp(), 'newfile.dat')
        fpath = np.memmap(filename, dtype='float64', mode='w+', shape=len(self.data))
        fpath[:-amount] = self.data[amount:]
        logging.info('{} {} shifted left'.format(self.name, amount))
        return Noise(name='{} time shifted left {}'.format(amount, self.name),
                     data=fpath, path='')

    def reverse(self):
        self.data = [ele for ele in reversed(self.data)]

    def draw(self):
        plt.figure(self.name, figsize=(12, 5))
        plt.title(self.name + ' Noise')
        time = np.arange(0, self.get_duration(), 1 / self.sample_rate)  # time vector
        plt.plot(time, self.data)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

    def draw_fft(self):
        self.init_fft()
        plt.figure(self.name + ' FFT')
        plt.plot(self.fft)
        plt.xlim([10, self.sample_rate / 2])
        plt.xscale('log')
        plt.grid(True)
        plt.xlabel('Frequency (Hz)')
        plt.show()

    def draw_all(self):
        plt.figure(self.name)
        plt.plot(self.data)
        plt.grid(True)
        plt.figure(self.name + ' FFT')
        plt.plot(self.fft)
        plt.xlim([10, self.sample_rate / 2])
        plt.xscale('log')
        plt.grid(True)
        plt.xlabel('Frequency (Hz)')
        plt.show()

    def draw_phase(self):
        plt.title(self.name + 'Phase spectrum')
        plt.phase_spectrum(self.data)
        plt.show()

    def convolve(self, other):
        return Noise(name='{} * {}'.format(self.name, other.name), data=np.convolve(self.data, other.data), path='')

    def hear_noise(self):
        return Audio(data=self.data, rate=self.sample_rate)

    def __mul__(self, other):
        return self.convolve(other)

    def __str__(self):
        return self.data
