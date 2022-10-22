from usbipy.client import usbipClient
import subprocess
import logging
log = logging.getLogger("usbipy")


class usbipHost(usbipClient):
    def __init__(self, debug = False, flags = []):
        usbipClient.__init__(self, debug, flags)
        log.info("Creating host")

    def bind(self, obj: str):
        try:
            return subprocess.getoutput(" ".join(self.usbip + ["bind", "-b", obj])).split("\n")
        except Exception as e:
            log.log(e)

    def unbind(self, obj: str):
        try:
            return subprocess.getoutput(" ".join(self.usbip + ["unbind", "-b", obj])).split("\n")
        except Exception as e:
            log.log(e)
