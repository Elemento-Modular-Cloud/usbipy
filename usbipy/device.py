import regex as re


class usbipyDevice():
    def __init__(self, busid=None, name=None, info=None, id=None, host=None):
        self.busid = self.set_busid(busid) if busid is not None else None
        self.name = name.replace("  ", "")[1:]
        self.info = info
        self.id = id
        self.host = host
        self.port = None

    def set_busid(self, busid: str):
        match = re.search("[0-9]{1,}-[0-9.]{1,}", busid)
        if match:
            return match.group()
        else:
            return None

    def __repr__(self):
        return f"{self.name} {self.info} ({self.busid}) [{self.id}]" + \
            (" "+ self.port if self.port is not None else "")
