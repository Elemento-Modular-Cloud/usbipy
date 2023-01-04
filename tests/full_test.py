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