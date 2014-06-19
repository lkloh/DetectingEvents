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

		# get the data of windows
		windowsE = self.separate_to_windows(self.hour_dataE)
		#windowsN = self.separate_to_windows(self.hour_dataN)
		#windowsZ = self.separate_to_windows(self.hour_dataZ)

		# get autocorrelation for windows
		self.compute_autocorrelation(windowsE)
	
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

	def compute_autocorrelation(self, data):
		numPts = len(data)
		autocorrelations = np.zeros(shape=(numPts, numPts))
		for i in xrange(numPts):
			current_comparison = data[i,:]
			for j in xrange(numPts):
				if i==j:  
					autocorrelations[i,i] = np.nan
				else:
					vec_j = data[j,:]
					autocorrelations[i,j] = np.corrcoef(current_comparison, vec_j)
		return autocorrelations
