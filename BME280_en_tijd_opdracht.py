import time
import smbus2
import bme280
address = 0x76
bus = smbus2.SMBus(1)
calibration_params = bme280.load_calibration_params(bus, address)
def celsuis_to_fahrenheit(celsuis):
    return (celsuis * 9/5) + 32
f=open("tabel_van_BME280_waardes.csv","a")
f.write(f"{"huidigetijd"}, {"tempC°"}, {"pressure"}, {"humidity"}, {"temp°F"} ")
f.write("\n")
f.close()
while True:
    try:
        data = bme280.sample(bus, address, calibration_params)
        temperature_celsuis = data.temperature
        pressure = data.pressure
        humidity = data.humidity
        temperature_fahrenheit = celsuis_to_fahrenheit(temperature_celsuis)
        time.sleep(5)
    except KeyboardInterrupt:
        print('Program stopped')
        break
    except Exception as e:
        print('An unexpected error occured:', str(e))
        break
    huidige_tijd = time.ctime()
    print(f"{huidige_tijd}, {temperature_celsuis: .1f}, {pressure: .1f}, {humidity: .1f}, {temperature_fahrenheit: .1f} ")
    f=open("tabel_van_BME280_waardes.csv","a")
    f.write(f"{huidige_tijd}, {temperature_celsuis: .1f}, {pressure: .1f}, {humidity: .1f}, {temperature_fahrenheit: .1f} ")
    f.write("\n")
    f.close()
    #NIET AF!!!!!!!!!