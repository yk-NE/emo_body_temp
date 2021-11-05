#!/usr/bin/env python3

#konashi
try:
    from asyncio.exceptions import CancelledError
except ModuleNotFoundError:
    from asyncio import CancelledError
from konashi import *
import konashi
from konashi.Settings import System as KonashiSystem
from konashi.Settings import Bluetooth as KonashiBluetooth
from konashi.Io import SoftPWM as KonashiSPWM
from konashi.Io import HardPWM as KonashiHPWM
from konashi.Io import Gpio as KonashiGpio
from konashi.Io import Analog as KonashiAin
from konashi.Io import I2C as KonashiI2C
from konashi.Builtin import Presence as KonashiPresence
from konashi.Builtin import AccelGyro as KonashiAccelGyro
from konashi.Builtin import Temperature as KonashiTemperature
from konashi.Builtin import Humidity as KonashiHumidity
from konashi.Builtin import Presence as KonashiPresence
from konashi.Builtin import RGBLed as KonashiRGB
import logging
import asyncio
import argparse
#emo
from emo import emo_send
#other
import math
import random


global END
END=False
global Presence
Presence=False
global RGB
RGB=[
        [0,0,0],
        [255,0,0],
        [0,255,0],
        [0,0,255],
        [255,255,255],
    ]
global alpha
alpha=255

async def main(device):
    global END
    try:
        if device is None:
            logging.info("Scan for konashi devices for 5 seconds")
            ks = await Konashi.search(5)
            if len(ks) > 0:
                device = ks[0]
                logging.info("Use konashi device: {}".format(device.name))
            else:
                logging.error("Could no find a konashi device")
                return
        try:
            await device.connect(5)
        except Exception as e:
            logging.error("Could not connect to konashi device '{}': {}".format(device.name, e))
            return
        logging.info("Connected to device")

        #function

        def input_cb(pin, level):
            if level:
                pass
            logging.info("Pin {}: {}".format(pin, level))
        # Input callback function set
        device.io.gpio.set_input_cb(input_cb)
        # GPIO0: enable, input, notify on change, pull-down off, pull-up off, wired function off
        # GPIO1~4: enable, output, pull-down off, pull-up off, wired function off
        await device.io.gpio.config_pins([
            (0x01, KonashiGpio.PinConfig(KonashiGpio.PinDirection.INPUT, KonashiGpio.PinPull.NONE, True)),
        ])
        d=0
        rd = await device.io.i2c.transaction(KonashiI2C.Operation.WRITE_READ,0x5a,3,bytes(0x7))
        print(rd)
        while True:
            await device.builtin.rgbled.set(RGB[d][0],RGB[d][1],RGB[d][2],alpha,100)
            await asyncio.sleep(1)
    except (asyncio.CancelledError, KeyboardInterrupt):
        logging.info("Stop loop")
        END=True
        await device.builtin.rgbled.set(RGB[d][0],RGB[d][1],RGB[d][2],0,1)
    finally:
        try:
            if device is not None:
                await device.disconnect()
                logging.info("Disconnected")
        except konashi.Errors.KonashiConnectionError:
            pass
    logging.info("Exit")


parser = argparse.ArgumentParser(description="Connect to a konashi device, setup the PWMs and control them.")
parser.add_argument("--device", "-d", type=Konashi, help="The konashi device name to use. Ommit to scan and use first discovered device.")
args = parser.parse_args()

logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()
main_task = None
try:
    main_task = loop.create_task(main(args.device))
    loop.run_until_complete(main_task)
except KeyboardInterrupt:
    if main_task is not None:
        main_task.cancel()
        loop.run_until_complete(main_task)
        main_task.exception()
finally:
    loop.close()