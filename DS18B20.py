from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
while True:
    temperature_in_celsuis = sensor.get_temperature()
    print(temperature_in_celsuis)
