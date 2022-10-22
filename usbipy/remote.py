from usbipy.client import usbipClient
import subprocess
import logging
log = logging.getLogger("usbipy")


class usbipRemote(usbipClient):
    def __init__(self, debug=False, flags = []):
        super().__init__(debug, flags)
        log.info("Creating remote client")

    def attach(self, remote: str, obj: str):
        try:
            return subprocess.getoutput(" ".join(self.usbip + ["attach", "-r", remote, "-b", obj])).split("\n")
        except Exception as e:
            log.log(e)

    def detach(self, remote: str, obj: str):
        try:
            return subprocess.getoutput(" ".join(self.usbip + ["unbind", "-r", remote, "-b", obj])).split("\n")
        except Exception as e:
            log.log(e)
    
    def list_remote(self, remote:str):
        try:
            return subprocess.getoutput(" ".join(self.usbip + ["unbind", "-r", remote])).split("\n")
        except Exception as e:
            log.log(e)
