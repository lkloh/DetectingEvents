import numpy as np
from scipy import signal
import matplotlib
matplotlib.rcParams['backend'] = "TkAgg"
import matplotlib.pyplot as py

class ReducingPointDensity:

	def __init__(self, original_signal_time, original_delta, reduce_factor):
		self.original_delta = original_delta
		self.original_num_pts = len(original_signal_time)
		self.reduce_factor = reduce_factor
		self.original_time = np.arange(0, self.original_num_pts*original_delta, original_delta)
		self.original_signal_time = original_signal_time

	def reducing_density(self):
		reduced_num_pts = int(self.original_num_pts / self.reduce_factor)+1
		reduced_time = np.zeros(shape=(reduced_num_pts, 1))
		for i in np.arange(0, self.original_num_pts, self.reduce_factor):
			index = int(i/self.reduce_factor)
			reduced_time[index] = self.original_signal_time[i]
		return reduced_time

	def plot_reduced(self):
		fig = py.figure()
		fig.suptitle('reduced')

		fig.plot(self.original_time, self.original_signal_time, label='Original')
		fig.plot(self.originalTime, filteredSignalTime, label='Filtered')
		fig.legend(loc="upper right")
		fig.set_title('Signal vs Time')