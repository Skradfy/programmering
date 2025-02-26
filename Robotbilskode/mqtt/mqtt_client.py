from machine import ADC, Pin

# Opsætning af ADC-kanal (brug Pin 26, ADC0)
adc = ADC(Pin(26))  # Pin 26 er ADC0 på Raspberry Pi Pico
# Konstant for at omregne ADC-værdien til spænding
ADC_REF_VOLTAGE = 3.3  # Pico's referenceniveau (3.3V)

import network
import utime
from umqtt.simple import MQTTClient

# Configure your WiFi SSID and password
ssid = 'ITEK 2nd'
password = '2nd_Semester_E24a'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    utime.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])

client = MQTTClient(client_id=b"kajsclient",
                    server=b"10.100.0.96",
                    port=0,
                    keepalive=7200)

client.connect()

def read_temperature():
    # Læs rå ADC-værdi (0-4095)
    raw_value = adc.read_u16()  # I MicroPython returnerer read_u16() en værdi mellem 0 og 65535
    # Konvertering af ADC-værdi til spænding (0V - 3.3V)
    voltage = (raw_value / 65535) * ADC_REF_VOLTAGE
    # Beregn temperaturen i Celsius
    temperature_celsius = voltage * 100
    return temperature_celsius

while True:
    print(read_temperature())
    client.publish('trek/22/tool/tmp35', str(read_temperature()))
    utime.sleep(2)
