from dronekit import connect
import mesajlar
import time

connection_string="127.0.0.1:14550"

iha = connect(connection_string,wait_ready=True,timeout=100)

while True:
    ms , usec = mesajlar.listen_SYSTEM_TIME(iha)
    print("mikro:" , usec, "    mili: ", ms)
    time.sleep(1)
