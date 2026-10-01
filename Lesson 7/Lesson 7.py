import time
from datetime import datetime

while True:
    dateNow = datetime.now()
    timeNow = dateNow.strftime("%H:%M:%S")
    print(f"\r{timeNow}", end="", flush=True)
    time.sleep(1)