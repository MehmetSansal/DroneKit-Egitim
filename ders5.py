from dronekit import connect

connection_string="127.0.0.1:14550"

iha=connect(connection_string,wait_ready=True,timeout=100)

print(iha.parameters['WPNAV_SPEED'])
iha.parameters['WPNAV_SPEED']=1000
print("Parametre degistirildi yeni deger: {}".format(iha.parameters['WPNAV_SPEED']))
