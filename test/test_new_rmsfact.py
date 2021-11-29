import unittest

import rmsfact


class TestNewRMSFact(unittest.TestCase):

    # The `_new_rmsfact()` function should return a function
    def test_new_rms_fact_returns_function(self):
        self.assert_(hasattr(rmsfact._new_rmsfact(), "__call__"))

    # `rmsfact.rmsfact()` should be a function
    def test_rmsfact_is_function(self):
        self.assert_(hasattr(rmsfact.rmsfact, "__call__"))

    # `rmsfact.rmsfact()` should return a string
    def test_returns_string(self):
        fact = rmsfact.rmsfact()
        self.assertIsInstance(fact, str)
