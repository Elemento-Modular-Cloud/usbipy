
from asyncio import subprocess

import subprocess
import logging
import regex as re

from usbipy.device import usbipyDevice
log = logging.getLogger("usbipy")
hdl = logging.StreamHandler()
hdl.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
log.addHandler(hdl)
log.setLevel(logging.DEBUG)


class usbipClient():
    def __init__(self, debug=False, flags=[]):
        log.info("Creating client")
        self.usbip = ["usbip"] + flags
        self.debug = debug
        if self.debug:
            self.usbip += ["-d"]

    def list(self, remote=None) -> list:
        devices = []
        if remote is None:
            try:
                out = subprocess.getoutput(
                    " ".join(self.usbip + ["list", "-l"])).split("\n")
                for bus, device_name in zip(out[::3], out[1::3]):
                    match = re.search("[a-z0-9]{4}:[0-9a-z]{4}", device_name)
                    _id = match.group() if match is not None else None
                    _name = device_name.split(":")[0][:-1]
                    _info = device_name.split(":")[1].split("(")[0]
                    dev = usbipyDevice(
                        name=_name, busid=bus, info=_info, id=_id)
                    devices.append(dev)
            except Exception as e:
                log.log(logging.ERROR, e)
        else:
            try:
                out = subprocess.getoutput(
                    " ".join(self.usbip + ["list", "-r", remote]))
                if "no exportable devices" in out:
                    raise Exception("no exportable devices")
                else:
                    out = out.split("\n")[3:]
                for iline, line in enumerate(out):
                    if re.findall("[0-9]{1,}-[0-9.]{1,}", line.split(":")[0]):
                        device_name = out[iline]
                        match = re.search("[a-z0-9]{4}:[0-9a-z]{4}", device_name)
                        _id = match.group() if match is not None else None
                        match = re.search("[0-9]{1,}-[0-9.]{1,}", device_name)
                        _busid = match.group()
                        _name = device_name.split(":")[1][:-1]
                        _info = device_name.split(":")[2].split("(")[0]
                        dev = usbipyDevice(
                            name=_name,
                            busid=_busid,
                            info=_info,
                            id=_id,
                            host=remote)
                        devices.append(dev)
            except Exception as e:
                log.log(logging.INFO, out)
                log.log(logging.ERROR, e)
        return devices

    def list_ports(self):
        log.info("Active ports:")
        try:
            out = subprocess.getoutput(
                " ".join(
                    self.usbip +
                    ["port"])).split("\n")[
                2:]
            for port, dev, busid in zip(out[::4], out[1::4], out[2::4]):
                port = port.split(":")[0]
                match = re.search("[0-9]{1,}", port)
                if match:
                    port = match.group()
                name = dev.replace("  ", "")
                match = re.search("[0-9]{1,}-[0-9.]{1,}", busid)
                if match:
                    _busid = match.group()
                else:
                    _busid = None
                print(f"Port {port} {name} {_busid}")
        except Exception as e:
            log.log(logging.ERROR, e)

    def get_port(self, device: usbipyDevice):
        try:
            out = subprocess.getoutput(
                " ".join(
                    self.usbip +
                    ["port"])).split("\n")[
                2:]
            for port, busid in zip(out[::4], out[2::4]):
                port = port.split(":")[0]
                match = re.search("[0-9]{1,}", port)
                if match:
                    port = match.group()
                match = re.search("[0-9]{1,}-[0-9.]{1,}", busid)
                if match:
                    _busid = match.group()
                else:
                    _busid = None
                if device.busid == _busid:
                    device.port = port
                    return True
        except Exception as e:
            log.log(logging.ERROR, e)
        return False

    def bind(self, device: usbipyDevice):
        try:
            out = subprocess.getoutput(
                " ".join(self.usbip + ["bind", "-b", device.busid])).split("\n")
            log.log(logging.INFO, out[0])
        except Exception as e:
            log.log(logging.ERROR, e)

    def unbind(self, device: usbipyDevice):
        try:
            out = subprocess.getoutput(
                " ".join(self.usbip + ["unbind", "-b", device.busid])).split("\n")
            log.log(logging.INFO, out[0])
        except Exception as e:
            log.log(logging.ERROR, e)

    def attach(self, device: usbipyDevice):
        try:
            out = subprocess.getoutput(" ".join(
                self.usbip + ["attach", "-r", device.host, "-b", device.busid])).split("\n")
            log.log(logging.INFO, out[0])
        except Exception as e:
            log.log(logging.ERROR, e)

    def detach(self, device: usbipyDevice):
        try:
            if device.port is None:
                if not self.get_port(device):
                    raise Exception("Cannot find device port")
            out = subprocess.getoutput(" ".join(self.usbip + ["detach", "-p", device.port])).split("\n")
        except Exception as e:
            log.log(logging.ERROR, e)
