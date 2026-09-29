import time
from gpiozero import LED
import board
import adafruit_dht
from DS18B20 import W1ThermSensor, Unit

Green = LED(5)
Orange = LED(6)
Red = LED(13)
teller = 0
dhtDevice = adafruit_dht.DHT11(board.D18)
sensor = W1ThermSensor()
while True:
    teller = teller + 1
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
    
        time.sleep(2.5)
        temperature_in_celsuis = sensor.get_temperature()
        temperature_in_all_units = sensor.get_temperatures([
            Unit.DEGREES_C])
        difference = temperature_in_celsuis - temperature_c
        if difference < 1:
            Green.on
            Orange.off
            Red.off
        elif 1 > difference <= 5:
            Orange.on
            Green.off
            Red.off
        elif difference > 5:
            Red.on
            Orange.off
            Green.off
        print(f"{teller}. DHT: {temperature_c:.1f} C")
        teller = teller + 1
        print(f"{teller}. W1thermsensor: {temperature_in_celsuis:.1f} C")
        teller = teller + 1
        print(f"{teller}. Difference: {difference:.1f}")
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.5)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    

