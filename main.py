import threading
from LastFM import loop

loop_thread = threading.Thread(target=loop)
loop_thread.start()