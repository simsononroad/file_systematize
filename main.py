import os
import platform
from pathlib import Path


courrent_os = platform.system()


def linux():
    pass


def windows():
    path = Path.cwd()
    file = os.listdir(path)
    
    for files in file:
        print(files)

if courrent_os == "Windows":
    windows()
elif courrent_os == "Linux":
    linux()