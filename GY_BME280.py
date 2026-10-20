import time
import smbus2
import bme280
address = 0x76
bus = smbus2.SMBus(1)
calibration_params = bme280.load_calibration_params(bus, address)
def celsuis_to_fahrenheit(celsuis):
    return (celsuis * 9/5) + 32
while True:
    try:
        data = bme280.sample(bus, address, calibration_params)
        temperature_celsuis = data.temperature
        pressure = data.pressure
        humidity = data.humidity
        temperature_fahrenheit = celsuis_to_fahrenheit(temperature_celsuis)
        print("Temperature {:.2f} °C, {:.2f} °F".format(temperature_celsuis, temperature_fahrenheit))
        print("Pressure {:.2f} hPa".format(pressure))
        print("Humidity: {:.2f} %".format(humidity))
        time.sleep(2)
    except KeyboardInterrupt:
        print('Program stopped')
        break
    except Exception as e:
        print('An unexpected error occured:', str(e))
        break