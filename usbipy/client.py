
from asyncio import subprocess

import subprocess
import logging
log = logging.getLogger("usbipy")
hdl = logging.StreamHandler()
hdl.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
log.addHandler(hdl)
log.setLevel(logging.DEBUG)


class usbipClient():
    def __init__(self, debug = False, flags = []):
        log.info("Creating client")
        self.usbip = ["usbip"] + flags
        self.debug = debug
        if self.debug:
            self.usbip += ["-d"]

    def list(self):
        try:
            return subprocess.getoutput(" ".join(self.usbip + ["list", "-l"])).split("\n")
        except Exception as e:
            log.log(e)

    def port(self):
        try:
            return subprocess.getoutput(" ".join(self.usbip + ["port"])).split("\n")
        except Exception as e:
            log.log(e)
            