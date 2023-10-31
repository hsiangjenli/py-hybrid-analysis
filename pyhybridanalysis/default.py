import requests
from enum import Enum

api_v2 = "https://www.hybrid-analysis.com/api/v2/"

class Environment(Enum):
    r"""
    ::

        Hybrid Analysis provides a wide range of environments for malware analysis.

    """
    mac = 400
    ubuntu2004 = 310
    ubuntu1604 = 300
    android = 200
    win10 = 160
    win7_64 = 120
    win7_32_hwp = 110
    win7_32 = 100

    @staticmethod
    def list_available():
        """

        .. admonition:: all available environments
            :class: info
        
            - 400: 'Mac Catalina 64 bit (x86)'
            - 310: 'Linux (Ubuntu 20.04, 64 bit)'
            - 300: 'Linux (Ubuntu 16.04, 64 bit)'
            - 200: 'Android Static Analysis'
            - 160: 'Windows 10 64 bit'
            - 120: 'Windows 7 64 bit'
            - 110: 'Windows 7 32 bit (HWP Support)'
            - 100: 'Windows 7 32 bit'
        """
        return Environment.__dict__["_member_map_"]

class BASE:
    def __init__(self, host: str=api_v2, api_key: str=None) -> None:
        self.host = host
        self.api_key = api_key
    
    @property
    def _header(self):
        return {"api-key": self.api_key, "user-agent": "Falcon"}

    def _post(self, url, data: dict, headers: dict):
        r = requests.post(url=url, data=data, headers=headers)
        return r.status_code, r