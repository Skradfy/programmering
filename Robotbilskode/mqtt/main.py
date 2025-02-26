import network
import utime
#Configure your WiFi SSID and password
ssid = 'ITEK 2nd'
password = '2nd_Semester_E24a'
wlan = network.WLAN(network.STA_IF) # network.STA_IF er en

wlan.active(True)
wlan.connect(ssid, password)
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...' )
    utime.sleep(1)
#Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed' )
else:
    print('connected')
status = wlan.ifconfig()
print('ip = ' + status[0])

import mip
mip.install("umqtt.simple")

