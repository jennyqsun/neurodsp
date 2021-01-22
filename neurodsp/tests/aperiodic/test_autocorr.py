"""Tests for neurodsp.aperiodic.autocorr."""

from neurodsp.aperiodic.autocorr import *

###################################################################################################
###################################################################################################

def test_compute_autocorr(tsig):

    timepoints, autocorrs = compute_autocorr(tsig)
    assert len(timepoints) == len(autocorrs)
