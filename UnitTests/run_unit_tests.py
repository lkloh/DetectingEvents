import unittest
from test_network_autocorrelation import networkAutocorrelationTests



"""Set """
suite_network_autocorrelation = unittest.TestLoader().loadTestsFromTestCase(networkAutocorrelationTests)


"""Run"""
unittest.TextTestRunner(verbosity=2).run(suite_network_autocorrelation)





