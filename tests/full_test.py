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

from usbipy import *
import time

cl = usbipClient()
local_devices = cl.list()
print(local_devices)

#cl.bind(local_devices[3])
# cl.unbind(local_devices[3])

remote_devices = cl.list(remote="10.0.0.102")

if len(remote_devices) > 0:
    cl.attach(remote_devices[0])
    time.sleep(10)
else:
    remote_devices = [usbipyDevice("5-1", "audio", "", "0d8c:0014", "10.0.0.102")]

cl.list_ports()
cl.get_port(remote_devices[0])
print(remote_devices)
cl.detach(remote_devices[0])