from dronekit import connect, VehicleMode
import time
connection_string="127.0.0.1:14550"
from pymavlink import mavutil
iha=connect(connection_string,wait_ready=True,timeout=100)
import math
def arm_ol_ve_yuksel(hedef_yukseklik):
	while iha.is_armable==False:
		print("Arm ici gerekli sartlar saglanamadi.")
		time.sleep(1)
	print("Iha su anda armedilebilir")
	
	iha.mode=VehicleMode("GUIDED")
	while iha.mode!='GUIDED':
		print('Guided moduna gecis yapiliyor')
		time.sleep(1.5)

	print("Guided moduna gecis yapildi")
	iha.armed=True
	while iha.armed is False:
		print("Arm icin bekleniliyor")
		time.sleep(1)

	print("Ihamiz arm olmustur")
	
	iha.simple_takeoff(hedef_yukseklik)
	while iha.location.global_relative_frame.alt<=hedef_yukseklik*0.94:
		print("Su anki yukseklik{}".format(iha.location.global_relative_frame.alt))
		time.sleep(0.5)
	print("Takeoff gerceklesti")

def pozisyon(posx, posy,yaw_rate,posz, iha):
	msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_LOCAL_NED, 
          0b0000011111111000,
          posx, posy, posz, #pozisyonlar(metre)
          0, 0, 0,#hizlar(metre/s)
          0, 0, 0,#akselarasyon(fonksiyonsuz)
          0, math.radians(yaw_rate))#yaw,yaw_rate(rad,rad/s)

        iha.send_mavlink(msg)
def f_cvt(x, y, angle):
	N = x*math.cos(angle) - y*math.sin(angle)
	E = x*math.sin(angle) + y*math.cos(angle)
	return N, E
arm_ol_ve_yuksel(15)
init_heading = (iha.heading / 180.0) * math.pi
a,b=f_cvt(5,0,init_heading)

pozisyon(a,b,0,-15,iha)
while iha.location.local_frame.north<=a*0.95:
	print("5 metre kuzeye ilerliyorum")
	time.sleep(1)
print("kuzeydeyim")
time.sleep(1)
init_heading = (iha.heading / 180.0) * math.pi
a,b=f_cvt(5,5,init_heading)
pozisyon(a,b,0,-15,iha)
while iha.location.local_frame.east<=b*0.95:
	print("5 metre doguya ilerliyorum")
	time.sleep(1)
print("dogudayim")
time.sleep(1)
init_heading = (iha.heading / 180.0) * math.pi
a,b=f_cvt(0,5,init_heading)
pozisyon(a,b,0,-15,iha)
while iha.location.local_frame.north>=0.1:
	print("5 metre guneye ilerliyorum")
	time.sleep(1)
print("guneydeyim")
time.sleep(1)
pozisyon(a,b,0,-20,iha)
while iha.location.local_frame.down<=19.8:
	print("5 metre daha yukariya ilerliyorum")
	time.sleep(1)
print("yukardayim")
time.sleep(1)

