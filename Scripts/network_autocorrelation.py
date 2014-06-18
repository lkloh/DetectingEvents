import numpy as np

class NetworkAutocorrelation:

	def __init__(self, delta, hour_dataE, hour_dataN, hour_dataZ, window_length, overlap_length):
		# save necessary data
		self.delta = delta
		self.hour_dataE = hour_dataE
		self.hour_dataN = hour_dataN
		self.hour_dataZ = hour_dataZ
		self.window_length = window_length
		self.overlap_length = overlap_length

		# run the functions
		windowsE = self.separate_to_windows(self.hour_dataE)
	
	def separate_to_windows(self, data):
		totalDataPoints = len(data)
		numPointsInWindow = int(self.window_length/self.delta)
		numPointsInOverlap = int(self.overlap_length/self.delta)

		numWindows = int((totalDataPoints-numPointsInWindow)/numPointsInOverlap + 1)

		splitToWindows = np.zeros(shape=(numWindows, numPointsInWindow))

		for i in xrange(numWindows):
			start_index = i*numPointsInOverlap
			for j in xrange(numPointsInWindow):
				splitToWindows[i,j] = data[start_index+j]

		return splitToWindows


