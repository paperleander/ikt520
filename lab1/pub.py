#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client("pub")
client.connect("localhost",1883,60)
client.publish("topic", "test", 0)
print("Published topic 'test'. Disconnecting")
client.loop_forever()
