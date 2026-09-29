import time

import board

import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D18)
while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(f"Temp: {temperature_f:.1f} F / {temperature_c:.1f} C   Humidity:  {humidity}%")
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)