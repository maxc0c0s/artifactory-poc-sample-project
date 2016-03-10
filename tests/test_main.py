import unittest
from sample.main import SampleClass

class TestMain(unittest.TestCase):
    def test_sample_add(self):
        sc = SampleClass()
        self.assertEqual(2, sc.add(1, 1))

