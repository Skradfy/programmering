from machine import Pin, PWM
import utime
import network
import gc

try:
    import usocket as socket
except:
    import socket

gc.collect()

ssid = 'xxxxxxx'
password = 'xxxxxxx'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    pass

print('Connection successful')
print(station.ifconfig())

led = Pin('LED', Pin.OUT)
led_state = "OFF"

pin14 = Pin(14, Pin.OUT)
pin15 = Pin(15, Pin.OUT)
pin13 = Pin(13, Pin.OUT)
pwm_pin = PWM(Pin(13))
pwm_pin.freq(1000)
gy53 = Pin(2, Pin.IN)


def down(speed):
    pin14.off()
    pin15.on()
    pin13.on()
    pwm_pin.duty_u16(int((65535 / 100) * speed))


def up(speed):
    pin15.off()
    pin14.on()
    pin13.on()
    pwm_pin.duty_u16(int((65535 / 100) * speed))


def stop():
    pin15.on()
    pin14.on()
    pin13.on()
    pwm_pin.duty_u16(0)


def get_distance():
    readings = []
    for _ in range(0.1):
        while gy53.value():
            pass
        while not gy53.value():
            pass
        starttime = utime.ticks_us()
        while gy53.value():
            pass
        endtime = utime.ticks_us()
        difference_in_us = endtime - starttime
        distance_mm = difference_in_us / 10
        readings.append(distance_mm)
        utime.sleep_ms(1)

    return sum(readings) / len(readings)


floor_heights = {
    "2": (50, 65),
    "1": (155, 165),
    "0": (225, 240)
}


def calculate_speed(distance, target_height_range):
    middle_point = (target_height_range[0] + target_height_range[1]) / 2
    distance_to_target = abs(distance - middle_point)

    max_speed = 35
    min_speed = 15
    deceleration_zone = 50

    if distance_to_target > deceleration_zone:
        return max_speed
    else:

        return max(min_speed, (max_speed - (distance_to_target / deceleration_zone) * (max_speed - min_speed)))


def adjust_speed(current_speed, target_speed):
    acceleration_rate = 2.5
    if current_speed < target_speed:
        return min(current_speed + acceleration_rate, target_speed)
    elif current_speed > target_speed:
        return max(current_speed - acceleration_rate, target_speed)
    return current_speed


def web_page():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Elevator</title>
<style>
  body {
    font-family: 'Georgia', serif;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f0f0f0;
  }
  .header {
    background-color: #f0f0f0;
    color: black;
    padding: 0px;
    text-align: center;
    margin-bottom: 0px;
    font-size: 60px;
  }
  .button-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative; /* Position relative for absolute positioning of the display */
  }
  .button {
    display: inline-block;
    padding: 15px 70px; /* Adjusted padding */
    margin: 10px;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    color: white;
    font-size: 30px;
    font-family: 'Georgia', serif;
  }
  .etage3, .etage2, .etage1 {
    background-color: #333;
  }
  .active {
    background-color: green;
  }
  .inactive {
    background-color: grey;
  }
</style>
</head>
<body>
<div class="header">Elevator</div>
<div class="button-container">
  <button class="button etage3" onclick="window.location.href='/floor/2'">2. Etage</button>
  <button class="button etage2" onclick="window.location.href='/floor/1'">1. Etage</button>
  <button class="button etage1" onclick="window.location.href='/floor/0'">0. Etage</button>
</div>
</body>
</html>"""
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    try:
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Received HTTP GET connection request from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('GET Request Content = %s' % request)

        floor2 = request.find('/floor/2')
        floor1 = request.find('/floor/1')
        floor0 = request.find('/floor/0')

        if floor2 == 6:
            user_input = "2"
        elif floor1 == 6:
            user_input = "1"
        elif floor0 == 6:
            user_input = "0"
        else:
            user_input = None

        if user_input in floor_heights:
            target_floor = user_input
            target_height_range = floor_heights[target_floor]
            print("Target floor:", target_floor)

            timeout = utime.ticks_ms() + 10000
            current_speed = 0

            while utime.ticks_ms() < timeout:
                distance = get_distance()
                print("Current distance:", distance)

                if target_height_range[0] <= distance <= target_height_range[1]:
                    stop()
                    print("Elevator stopped at floor", target_floor)
                    break

                target_speed = calculate_speed(distance, target_height_range)
                current_speed = adjust_speed(current_speed, target_speed)

                if distance > target_height_range[1]:
                    up(current_speed)
                    print("Moving up with speed:", current_speed)
                else:
                    down(current_speed)
                    print("Moving down with speed:", current_speed)

            else:
                print("Failed to reach the target floor within the timeout.")

        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')

