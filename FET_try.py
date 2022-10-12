import json



PowerPayload = {}

for i in range(3):
    PowerPayload["Power_Current0"+str(i)] = i*3
    PowerPayload["Power_Temp0"+str(i)] = i*3+1
    PowerPayload["Power_Battery0"+str(i)] = i*3+2
    
        
print (PowerPayload)