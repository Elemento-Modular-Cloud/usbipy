# #******************************************************************************#
# # Copyright(c) 2019-2023, Elemento srl, All rights reserved                    #
# # Author: Elemento srl                                                         #
# # Contributors are mentioned in the code where appropriate.                    #
# # Permission to use and modify this software and its documentation strictly    #
# # for personal purposes is hereby granted without fee,                         #
# # provided that the above copyright notice appears in all copies               #
# # and that both the copyright notice and this permission notice appear in the  #
# # supporting documentation.                                                    #
# # Modifications to this work are allowed for personal use.                     #
# # Such modifications have to be licensed under a                               #
# # Creative Commons BY-NC-ND 4.0 International License available at             #
# # http://creativecommons.org/licenses/by-nc-nd/4.0/ and have to be made        #
# # available to the Elemento user community                                     #
# # through the original distribution channels.                                  #
# # The authors make no claims about the suitability                             #
# # of this software for any purpose.                                            #
# # It is provided "as is" without express or implied warranty.                  #
# #******************************************************************************#
#
# #------------------------------------------------------------------------------#
# #Authors:                                                                      #
# #- Gabriele Gaetano Fronze' (gfronze at elemento.cloud)                        #
# #- Filippo Valle (fvalle at elemento.cloud)                                    #
# #------------------------------------------------------------------------------#
#

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