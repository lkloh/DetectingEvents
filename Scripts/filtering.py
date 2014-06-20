import numpy as np
from scipy import signal
import matplotlib
matplotlib.rcParams['backend'] = "TkAgg"
import matplotlib.pyplot as py

class FilterSignals:

	def __init__(self, originalSignalTime, delta, order, cornerFreq):
		self.originalSignalTime = originalSignalTime
		self.num_points = len(originalSignalTime)
		self.delta = delta
		self.order = order
		self.cornerFreq = cornerFreq
		self.originalTime = np.arange(0, self.num_points*delta, delta)

	def filtering(self):
		# plot original signal-vs-time
		fig = py.figure()
		fig.suptitle('FILTERING FREQUENCIES')

		# time -> frequency 
		# unfiltered
		originalSignalFreq = np.fft.fft(self.originalSignalTime)
		originalFreq = np.fft.fftfreq(self.num_points, self.delta)

		#filter the time signal
		NYQ = 1.0/(2*self.delta)

		Wn = self.cornerFreq/NYQ
		B, A = signal.butter(self.order, Wn, analog=False, btype='lowpass')

		w, h = signal.freqz(B,A)
		filteredSignalTime = signal.lfilter(B, A, self.originalSignalTime)

		# convert filtered time signal -> frequency signal
		filteredSignalFreq = np.fft.fft(filteredSignalTime)

		# PLOT TIME
		ax1 = fig.add_subplot(211)
		ax1.plot(self.originalTime, self.originalSignalTime, label='Original')
		ax1.plot(self.originalTime, filteredSignalTime, label='Filtered')
		ax1.legend(loc="upper right")
		ax1.set_title('Amplitude vs Time')

		# PLOT FREQUENCY
		# in Hertz
		ax2 = fig.add_subplot(212)
		ax2.plot(originalFreq, np.abs(originalSignalFreq), label='Original')
		ax2.plot(originalFreq, np.abs(filteredSignalFreq), label='Filtered')
		MULTIPLE = 0.7*max(np.abs(originalSignalFreq))
		ax2.plot(w*(NYQ/np.pi), MULTIPLE*np.abs(h), label='Butter Filter')
		ax2.legend(loc="upper right")
		ax2.set_title('Amplitude Spectrum vs frequency')
		ax2.set_xlim(0,0.1)

		py.show()


