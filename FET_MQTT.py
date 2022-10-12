# coding:utf-8
import codecs
import json
import ssl
import paho.mqtt.client as mqtt
import time


def PowerLoop():
    with open('static/data/PowerMeter.json', 'r') as f:
        data = json.load(f)
    f.close
    return data

def ReadMqttInfor():
    with open('static/data/mqttinfor.json', 'r') as f:
        data = json.load(f)
    f.close
    return data


def MqttPublish():
    try:
        Mqttinfor = ReadMqttInfor()
        PowerInfor = PowerLoop()
        MainLoop01  = [
            {"access_token": PowerInfor["MainLoop01"]["access_token"],
             "app": PowerInfor["MainLoop01"]["app"],
             "type": PowerInfor["MainLoop01"]["type"],
             "data": PowerInfor["MainLoop01"]["data"]}]
        print (Mqttinfor['appInfo']['MQTT_UserName'])
    
        client = mqtt.Client('', True, None, mqtt.MQTTv31)
        client.username_pw_set(Mqttinfor['appInfo']['MQTT_UserName'], Mqttinfor['appInfo']['MQTT_Password'])
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        client.tls_set_context(context)
        client.connect(Mqttinfor['appInfo']['MQTT_url'], Mqttinfor['appInfo']['MQTT_Port'], 60)
        client.loop_start()
        time.sleep(1)
        data02 = client.on_connect
        data03 = client.publish(Mqttinfor['appInfo']['MQTT_topic'],json.dumps(MainLoop01))
        time.sleep(3)
        client.loop_stop()
        client.disconnect()
        time.sleep(10)
        return ('OK')
    except:
        return ('error')

def Pub_infor():
    try:
        Mqttinfor = ReadMqttInfor()
        PowerInfor = PowerLoop()
        MainLoop01  = [
            {"access_token": PowerInfor["MainLoop01"]["access_token"],
             "app": PowerInfor["MainLoop01"]["app"],
             "type": PowerInfor["MainLoop01"]["type"],
             "data": PowerInfor["MainLoop01"]["data"]}]
        print (Mqttinfor['appInfo']['MQTT_UserName'])
    
        client = mqtt.Client('', True, None, mqtt.MQTTv31)
        client.username_pw_set(Mqttinfor['appInfo']['MQTT_UserName'], Mqttinfor['appInfo']['MQTT_Password'])
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        client.tls_set_context(context)
        client.connect(Mqttinfor['appInfo']['MQTT_url'], Mqttinfor['appInfo']['MQTT_Port'], 60)
        client.loop_start()
        time.sleep(1)
        data02 = client.on_connect
        data03 = client.publish(Mqttinfor['appInfo']['MQTT_topic'],json.dumps(MainLoop01))
        time.sleep(3)
        client.loop_stop()
        client.disconnect()
        time.sleep(10)
        return ('OK')
    except:
        return ('error')
        
if __name__ == '__main__':
    while True:
        #PowerLoop()
        MqttPublish()
        time.sleep(10)