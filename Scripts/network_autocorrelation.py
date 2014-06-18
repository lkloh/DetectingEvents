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

	
	def separate_to_windows(self, data):


