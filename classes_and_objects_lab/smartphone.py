from typing import List

class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps: List[str] = []
        self.is_on: bool = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int) -> str:
        if not self.is_on:
            return f"Turn on your phone to install {app}"

        if self.memory > app_memory:
            self.memory -= app_memory
            self.apps.append(app)

            return f"Installing {app}"

        return f"Not enough memory to install {app}"

    def status(self) -> str:
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"