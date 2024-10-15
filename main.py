scriptMain = "Main"
versionMain = "v0.2.0"

import threading
from LastFM import loop
import time

def logFormat():
    return f"{time.strftime("[%H:%M:%S - %d/%m/%Y]")} | {scriptMain} {versionMain}"

print(f"{logFormat()} Using LastFM for activity data.")
loop_thread = threading.Thread(target=loop)
loop_thread.start()