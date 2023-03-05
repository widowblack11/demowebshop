from dataclasses import dataclass
from os import getenv


@dataclass
class Hosts:
    def __init__(self, env):
        self.demoqa = getenv(f'{env.upper()}_DEMOQA')
        self.reqres = getenv(f'{env.upper()}_REQRESIN')
