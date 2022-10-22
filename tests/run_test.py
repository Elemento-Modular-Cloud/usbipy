import unittest
import os,sys
sys.path.append(os.getcwd())
from usbipy import *

class UsbIPTest(unittest.TestCase):
    def test_import(self):
        import usbipy
        self.assertTrue(True)

    def test_istances(self):
        cl = usbipClient()
        self.assertIsInstance(cl, usbipClient)
        cl = usbipHost()
        self.assertIsInstance(cl, usbipHost)
        cl = usbipRemote()
        self.assertIsInstance(cl, usbipRemote)

    def test_list(self):
        for cl in [usbipClient(), usbipHost(), usbipRemote()]:
            cl.usbip = ["echo"]
            self.assertEqual(cl.list(), ["list -l"])

if __name__ == "__main__":
    unittest.main()