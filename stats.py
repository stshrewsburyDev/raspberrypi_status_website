import psutil, subprocess
from requests import get as requests
from os import getenv
from time import sleep
from threading import Thread
from datetime import datetime


class Stats:
    def __init__(self, update_interval):
        self.last_update = datetime.now()
        self.update_interval = update_interval
        self.CHECK_PYPI = int(getenv("CHECK_PYPI"))
        self.process = Thread(target=self.update)
        self.PIP = getenv("PIP").split(" ")
        self.PIP.append("show")
        self.libraries = [{"lib": lib, "ver": "Unknown", "pypi": None} for lib in getenv("LIBRARIES").split(":")]
        self.CPU = {"percent": 0, "temp": None}
        self.RAM = {"percent": 0, "total": 0, "used": 0}
        self.SWAP = {"percent": 0, "total": 0, "used": 0}
        self.DISK = {"percent": 0, "total": 0, "used": 0}

    def get_ver(self, lib):
        try:
            cmd = self.PIP.copy()
            cmd.append(lib)
            result = str(subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode('UTF-8')).lower().split("\n")
            for line in result:
                if line.startswith("version:"):
                    line.replace("/r", "")
                    return line.split(" ")[1]
        except:
            return "Unknown"

    def get_pypi_ver(self, lib):
        if not self.CHECK_PYPI:
            return None
        with requests(f"https://pypi.org/pypi/{lib}/json") as r:
            if r.status_code == 200:
                data = r.json()['info']
                return data['version'] if 'version' in data else None
        return None

    def update(self):
        while True:
            ram = psutil.virtual_memory()
            swap = psutil.swap_memory()
            disk = psutil.disk_usage("/")
            temps = psutil.sensors_temperatures() if hasattr(psutil, "sensors_temperatures") else {}
            temp = temps['cpu_thermal'] if 'cpu_thermal' in temps else None

            self.CPU["percent"] = psutil.cpu_percent(interval=1)
            self.CPU["temp"] = temp[0].current if temp else None
            self.RAM = {"percent": ram.percent, "total": ram.total, "used": ram.used}
            self.SWAP = {"percent": swap.percent, "total": swap.total, "used": swap.used}
            self.DISK = {"percent": disk.percent, "total": disk.total, "used": disk.used}

            self.libraries = [{"lib": lib['lib'], "ver": self.get_ver(lib['lib']), "pypi": self.get_pypi_ver(lib['lib'])} for lib in self.libraries]

            self.last_update = datetime.now()

            sleep(self.update_interval)

    def start(self):
        self.process.start()
