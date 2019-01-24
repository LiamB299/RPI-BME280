#!/usr/bin/env python2.7

import smbus2
import bme280 as bm
import time

port = 1
address = 0x76
bus = smbus2.SMBus(port)

while True:
        calibration_params = bm.load_calibration_params(bus, address)
        data = bm.sample(bus, address, calibration_params)
        print(data.temperature)
        time.sleep(3)


