# Sound Recognition with Python

## First Of All
Clone or Download project and ...
```python
import Sound
```
## Sound simulation
* Initialize a Sound module with 
```python
s = Sound.Sound(path='path.wav')
```
or
```python
s = Sound.Sound(path='path.wav',name='mySound')
```

* Initialize FFT(Fast Fourier transform) on our Sound module
```python
s.initFFT()
print(s.getFFT())
s.drawFFT()
```
* Sound schematics
```python
s.draw() #Sound Digital Schematic
s.drawFFT() #Sound FFT Schematic
```

* Requirements
```bash
pip install scipy
pip install matplotlib
```
