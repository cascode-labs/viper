import unittest
import tempfile
import os
from virt.cdslib import include_cdslib

class Cdslib(unittest.TestCase):
    def setUp(self):
        self.test_path = tempfile.mkdtemp(prefix="virt_cdslib_")
        self.cdslib_path = os.path.join(self.test_path,"cds.lib")

    def test_add_library(self):
        self.assertEqual(True, False)

    def test_include_existing(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
