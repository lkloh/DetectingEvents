import obspy as obs
from filtering import FilterSignals
from reducing import ReducingPointDensity
from network_autocorrelation import NetworkAutocorrelation

"""only one station is used"""

"""read in the SAC files"""
bhe_stream = obs.read('../M43A/TA.M43A..BHE.M.2012.169.201502.SAC')[0]
bhn_stream = obs.read('../M43A/TA.M43A..BHN.M.2012.169.201502.SAC')[0]
bhz_stream = obs.read('../M43A/TA.M43A..BHZ.M.2012.169.201502.SAC')[0]

print dir(bhe_stream)


"""setting variables"""
delta = bhz_stream.stats.delta
window_length = 30
overlap_length = 0.4

"""try to filter"""
filter_order = 3
filter_cornerFreq = 5
# ftr = FilterSignals(bhe_stream.data, delta, filter_order, filter_cornerFreq)
# ftr.filtering()

"""reduce density"""
reduced_array = ReducingPointDensity(bhe_stream.data, delta, 100)



#NetworkAutocorrelation(delta, bhe_stream.data, bhn_stream.data, bhz_stream.data, window_length, overlap_length)
