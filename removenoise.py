import numpy as np
import scipy as sp
from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy import signal


(Frequency, array) = read('output.wav')

FourierTransformation = sp.fft.fft(array)

scale = np.linspace(0, Frequency, len(array))
GuassianNoise = np.random.rand(len(FourierTransformation))


NewSound = GuassianNoise + array

write("New-Sound-Added-With-Guassian-Noise.wav", Frequency, NewSound)

b,a = signal.butter(5, 1000/(Frequency/2), btype='highpass')

filteredSignal = signal.lfilter(b,a,NewSound)



c,d = signal.butter(5, 380/(Frequency/2), btype='lowpass') # ButterWorth low-filter
newFilteredSignal = signal.lfilter(c,d,filteredSignal) # Applying the filter to the signal

write("foutput.wav", Frequency, newFilteredSignal)
