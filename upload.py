#!/usr/bin/env python2.7

import datetime
import paho.mqtt.client as mqtt
import random as rnum
import time as sl
import smbus2
import bme280

def temp_collect():
        bus = smbus2.SMBus(1)
        cal_p = bme280.load_calibration_params(bus, 0x76)
        data = bme280.sample(bus, 0x76, cal_p)
        return data.temperature

def on_connect(client, userdata, flags, rc):
        print("Connection established")

def on_log(client, userdata, level, buf):
        print("log: ",buf)


def on_disconnect(client, userdata, rc):
        print("Disconnected from server. Check Network connection.")
        client.reconnect()

def on_publish(client, userdata, mid):
        print("Message sent succesfully")


broker = 
user = 
password = 
port = 

def main():
        client = mqtt.Client("Pi",False)
        client.username_pw_set(user,password)
        client.connect_async(broker,port,60) #1883,60
        client.on_connect=on_connect
        client.loop_start()
        client.max_inflight_messages_set(30)
        text = ""
        while True:
                temp = temp_collect()
                date = datetime.datetime.now().strftime("%d/%m/%Y")
                time = datetime.datetime.now().strftime("%H:%M:%S")
                upload = str(temp)+"&"+time+"&"+date
                #print(upload)
                client.publish("PiTest", upload, 1)
                sl.sleep(15)
                client.on_log=on_log
                client.on_disconnect=on_disconnect
                client.on_publish=on_publish
        client.loop_stop()
        return 0;


main()


