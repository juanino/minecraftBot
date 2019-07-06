#!/usr/bin/python3

from subprocess import Popen
import subprocess
import sys

filename = "mc-control.py"
while True:
    print("\nStarting " + filename)
    p = Popen("python3 " + filename, shell=True)
    p.wait()
    subprocess.run(["python3", "send_discord.py", "Minecraft bot died,  and issuing a restart"])
