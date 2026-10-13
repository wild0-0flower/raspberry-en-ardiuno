from gpiozero import MCP3008
from time import sleep
import time
import board
import adafruit_dht
dhtDevice = adafruit_dht.DHT11(board.D18)
teller = 0
while True:
    Digi_waarde = MCP3008(channel = 0)
    spannings_waarde = (Digi_waarde.value / 1) * 3.3
    sleep(1)
    temp =  (spannings_waarde - 0.5) / 0.01
    try:
        temperature_c = dhtDevice.temperature
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(3.0)
    teller = teller + 1
    gemm_temp = (temperature_c + temp) / 2
    verschil = temperature_c - temp
    f=open("waardes DHT en TMP36.csv","a")
    print(f"{teller}, {temperature_c: .1f},{temp: .1f},{gemm_temp: .1f},{verschil: .1f} ")
    f.write(f"{teller},{temperature_c: .1f},{temp: .1f},{gemm_temp: .1f},{verschil: .1f} ")
    f.write("\n")
    
    f.close()


    
    



