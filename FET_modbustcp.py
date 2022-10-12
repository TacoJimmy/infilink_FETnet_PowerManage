import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import struct
import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time

def getPowerLoop01(HOST_Addr, HOST_Port):
    try:
        PowerPayload = {}
        master = modbus_tcp.TcpMaster(host=HOST_Addr,port=HOST_Port)
        master.set_timeout(5.0)
        clamp_meter = master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 27)
        for i in range(8):    
            PowerPayload["Power_Current0"+str(i)] = clamp_meter[i*3]
            PowerPayload["Power_Temp0"+str(i)] = clamp_meter[i*3+1]
            PowerPayload["Power_Battery0"+str(i)] = clamp_meter[i*3+2]
            PowerPayload["Power_Flag"] = 1
    except:
        PowerPayload = {}
        for i in range(8):    
            PowerPayload["Power_Current0"+str(i)] = 9999
            PowerPayload["Power_Temp0"+str(i)] = 9999
            PowerPayload["Power_Battery0"+str(i)] = 9999
            PowerPayload["Power_Flag"] = 1
    return PowerPayload


def getPowerLoop02(HOST_Addr, HOST_Port):
    try:
        PowerPayload = {}
        master = modbus_tcp.TcpMaster(host=HOST_Addr,port=HOST_Port)
        master.set_timeout(5.0)
        clamp_meter = master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 27)
        for i in range(8):    
            PowerPayload["Power_Current0"+str(i)] = clamp_meter[i*3]
            PowerPayload["Power_Temp0"+str(i)] = clamp_meter[i*3+1]
            PowerPayload["Power_Battery0"+str(i)] = clamp_meter[i*3+2]
    except:
        PowerPayload = {}
        for i in range(8):    
            PowerPayload["Power_Current0"+str(i)] = 9999
            PowerPayload["Power_Temp0"+str(i)] = 9999
            PowerPayload["Power_Battery0"+str(i)] = 9999
    return PowerPayload


def SavePowerLoop():
    PowerLoop01 = getPowerLoop01('HOST_Addr', 'HOST_Port')
    with open('static/data/PowerLoop01.json', 'w') as f:
        json.dump(PowerLoop01, f)
    f.close
    
    PowerLoop02 = getPowerLoop01('HOST_Addr', 'HOST_Port')
    with open('static/data/PowerLoop02.json', 'w') as f:
        json.dump(PowerLoop02, f)
    f.close
    
def CleanPowerFlag():
    with open('static/data/PowerLoop01.json', 'r') as f:
        Power_data = json.load(f)
    Power_data["Power_Flag"] = 0
    with open('static/data/PowerLoop01.json', 'w') as g:
        json.dump(Power_data, g)
    f.close
    
if __name__ == '__main__':
    SavePowerLoop()
    CleanPowerFlag()