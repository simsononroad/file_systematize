import os
import platform
from pathlib import Path


courrent_os = platform.system()


def linux():
    pass
py = ".py"

def windows():
    path = Path.cwd()
    file = os.listdir(path)

    for files in file:

        if ".py" in files:
            try:
                os.mkdir("python")
            except FileExistsError:
                pass
            dest = "python"
            file_p_des = f"{dest}/{files}"
            os.rename(files, file_p_des)
        elif ".png" in files or ".jpg" in files:
            os.mkdir("kepek")
            dest = "kepek"
            file_p_des = f"{dest}/{files}"
            os.rename(files, file_p_des)
        elif ".json" in files:
            os.mkdir("json")
            dest = "json"
            file_p_des = f"{dest}/{files}"
            os.rename(files, file_p_des)
        elif ".pdf" in files:
            os.mkdir("pdf")
            dest = "pdf"
            file_p_des = f"{dest}/{files}"
            os.rename(files, file_p_des)


if courrent_os == "Windows":
    windows()
elif courrent_os == "Linux":
    linux()