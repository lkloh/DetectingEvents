import obspy as obs

"""read in the SAC files"""
bhe_stream = obs.read('M43A/TA.M43A..BHE.M.2012.169.201502.SAC')

print bhe_stream