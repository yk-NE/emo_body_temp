#!/usr/bin/env python3
import smbus
import sys
from emo import *
from bodytemp import *

addr=0x5a#i2cアドレス
bus = smbus.SMBus(1)
bt=BodyTemp(True)
sendflag=False
while True:
    try:
        Atemp = bus.read_i2c_block_data(addr,0x6,3)
        Otemp = bus.read_i2c_block_data(addr, 0x7, 3)
        bt.read(Otemp)
        btemp,l=bt.bodytemp()
        if btemp!=-1 and l>15 and not sendflag:
            msg="体温は"+str(btemp)+"度だよ"
            #emo_send(msg,[255,0,0])
            sendflag=True
        else:
            sendflag=False
    except KeyboardInterrupt:
        sys.exit(1)