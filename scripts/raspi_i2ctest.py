import smbus
import time

addr=0x5a
bus = smbus.SMBus(1)
Atemp = bus.read_i2c_block_data(addr,0x6,3)
Otemp = bus.read_i2c_block_data(addr, 0x7, 3)
AmbientTemp = ((Atemp[1]*256 + Atemp[0]) *0.02 -273.15)
ObjectTemp = ((Otemp[1]*256 + Otemp[0]) *0.02 -273.15)
htemp=ObjectTemp-AmbientTemp
print(AmbientTemp,ObjectTemp,"/",round(htemp,1),"℃")