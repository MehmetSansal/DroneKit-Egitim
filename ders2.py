from dronekit import connect

connection_string="127.0.0.1:14550"

iha=connect(connection_string,wait_ready=True,timeout=100)

print(iha.location.global_relative_frame.alt)
