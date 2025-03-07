import numpy as np
import pytest

from cmeutils.plotting import get_histogram
from cmeutils.plotting import threedplot

from base_test import BaseTest


class TestPlotting(BaseTest):
    def test_histogram_bins(self):
        sample = np.random.randn(100)
        bin_c, bin_h = get_histogram(sample, bins=20)
        assert len(bin_c) == len(bin_h) == 20

    def test_histogram_normalize(self):
        sample = np.random.randn(100)*-1
        bin_c, bin_h = get_histogram(sample, normalize=True)
        assert all(bin_h <= 1)

    def test_3dplot(self):
        x = [1,2,3,4,5]
        y = [1,2,3,4,5]
        z = [1,2,3,4,5]
        threedplot(x,y,z)

