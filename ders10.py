from dronekit import connect

connection_string="/dev/serial/by-id/usb-Hex_ProfiCNC_CubeOrange_3B0037000351303237343537-if00" #buraya kendi gorev bilgisayarinizda komut ekranina "ls /dev/serial/by-id/" yazdiktan sonra cikar portu tum directory ile beraber giriniz. Bu benim bilgisayara takdigim pixhawk cube orange'in portu. Sizin pixhawkinizin portunun pathi elbette farkli olacaktir.

iha=connect(connection_string,wait_ready=True,timeout=100,baud=115200)

print(iha.location.global_relative_frame.alt)

