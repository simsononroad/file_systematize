import os
import platform
from pathlib import Path
from rich.console import Console


courrent_os = platform.system()
consol = Console()
file_helyek = [["python", [".py"]], 
               ["kepek", [".png", ".jpg"]], 
               ["json", [".json"]],
               ["pdf", [".pdf"]],
               ["hang", [".wav", ".m4a", ".mp3"]],
               ["videok", [".mp4"]]]


szamolas = 1
def move(folder_name, files):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        pass
    dest = folder_name
    file_p_des = f"{dest}/{files}"
    os.rename(files, file_p_des)



path = Path.cwd()
fileok = os.listdir(path)
consol.print(f"Jelenlegi operációsrendszer: [bold blue]{courrent_os}[/bold blue]")
for file in fileok:
    for file_hely in file_helyek:
        for extension in file_hely[1]:
            if extension in file:
                ertek = move(file_hely[0], file)
                break

