# Process sounds easy on python :headphones:

## First Of All
Clone or Download project and import "sound.py" to your code:
```python
import sound
```
## Create a Noise
* import Noise class from "sound.py" and initial it with a Wav file or byte array of a sound:
```python
Import Noise from sound
noise1 = Noise(path='./M1.wav', name='Mic 1')

# plot your noise
noise1.draw()
```
Method | Usage
------- | -------
parse_wav() | parse wav file to byte array
init_fft() | initials fft of noise
get_fft() | returns fft of noise
get_energy() | returns energy (power) of noise
get_duration() | returns duration of noise in seconds
get_slice() | returns slice of noise like 2 seconds of noise
get_max() | returns upper bound of amplitude
when_max() | returns when upper bound happends in seconds
shift_right() | shifts noise signal to right in time domain
shift_left() | shifts noise signal to left in time domain
reverse() | reverses noise
convolve(other) | convolve the noise to another or use '*' operator like 'n1 * n2'
draw() | plot the noise in time domain
draw_fft() | plot the noise fft in frequency domain
draw_all() | plot the noise and fft both
draw_phase() | plot phase of voise in frequency domain
hear_noise() | returns IPython.display.audio object to hear noise in Jupyter Notebook


## Requirments
  * matplotlib==3.3.0
  * numpy==1.19.1
  * scipy==1.5.1
  * ipython==7.16.1
  * For better experince install "Jupyter Notebook"
  
