from sound import Noise,Hn
#
# s1 = Noise(path='./M1.wav', name='M1')
# s1.draw_fft()
#
# s2 = Noise(path='./M2.wav', name='M2')
# s2.draw_fft()
# #
s3 = Noise(path='./M3.wav', name='M3')
shifted = s3.shift_right(0.001)
# s3.draw()
# s3.hear_noise()
# print(s3.when_max())
# Reading Hn
hn = Hn(path='./Hn.txt')
# hn.draw()

# conv = s3.convolve(hn)
# print(conv.get_duration())
# slc = conv.get_slice(float(0.2))
# print(slc.get_duration())
# slc_conv = slc.convolve(conv)
# slc_conv.draw()


