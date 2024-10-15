scriptMain = "Main"
versionMain = "v0.2.1"

import threading
from LastFM import loop
import time
import config

if __name__ == "__main__":
    def logFormat():
        return f"{time.strftime("[%H:%M:%S - %d/%m/%Y]")} | {scriptMain} {versionMain}"

    if config.activityMethod.lower() == "lastfm":
        print(f"{logFormat()} Using LastFM for activity data.")
        loop_thread = threading.Thread(target=loop)
        loop_thread.start()