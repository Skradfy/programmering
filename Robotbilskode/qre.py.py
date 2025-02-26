from machine import Pin, PWM, Timer
import time

# Motor Pins (PWM for speed control)
motor1_in1 = PWM(Pin(3))  # GPIO 3 - IN1 (PWM for motor 1)
motor1_in2 = PWM(Pin(4))  # GPIO 4 - IN2 (PWM for motor 1)
motor2_in3 = PWM(Pin(4))  # GPIO 4 - IN3 (PWM for motor 2)
motor2_in4 = PWM(Pin(5))  # GPIO 5 - IN4 (PWM for motor 2)

# Set PWM frequency for motors (adjust as necessary)
motor1_in1.freq(1000)  # 1 kHz frequency
motor1_in2.freq(1000)
motor2_in3.freq(1000)
motor2_in4.freq(1000)

# QRE1113 sensor pin
qre1113_sensor = Pin(27, Pin.IN)

# ToF sensor setup using PWM
tof_pwm_pin = Pin(6, Pin.IN)

pulse_start = 0
pulse_width = 0


# Interrupt handler to capture PWM signal from ToF sensor
def pwm_callback(pin):
    global pulse_start, pulse_width
    if pin.value() == 1:  # Rising edge
        pulse_start = time.ticks_us()
    else:  # Falling edge
        pulse_width = time.ticks_diff(time.ticks_us(), pulse_start)


# Attach interrupt to capture PWM signal from the distance sensor
tof_pwm_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=pwm_callback)


# Convert PWM pulse width to distance (adjust as needed for your sensor)
def get_distance_from_pwm():
    global pulse_width
    distance = pulse_width / 10  # Conversion factor (adjust according to sensor specs)
    return distance


# Function to set motor speed using PWM
def set_motor_speed(motor_pwm, speed):
    duty_cycle = int(65535 * (speed / 100))  # Duty cycle: 0-65535
    motor_pwm.duty_u16(duty_cycle)  # Set duty cycle in 16-bit resolution


# Function to move the robot forward
def move_forward(speed=100):
    set_motor_speed(motor1_in1, speed)
    set_motor_speed(motor1_in2, 0)
    set_motor_speed(motor2_in3, speed)
    set_motor_speed(motor2_in4, 0)


# Function to stop the robot
def stop_robot():
    set_motor_speed(motor1_in1, 0)
    set_motor_speed(motor1_in2, 0)
    set_motor_speed(motor2_in3, 0)
    set_motor_speed(motor2_in4, 0)


# Function to turn around
def turn_around(speed=50):
    set_motor_speed(motor1_in1, 0)
    set_motor_speed(motor1_in2, speed)  # Reverse motor 1
    set_motor_speed(motor2_in3, speed)  # Motor 2 forward
    set_motor_speed(motor2_in4, 0)
    time.sleep(1)


# Function to turn toward the obstacle
def turn_toward_obstacle(speed=50):
    while get_distance_from_pwm() > 300:  # Assuming obstacle not directly in front
        set_motor_speed(motor1_in1, speed)
        set_motor_speed(motor1_in2, 0)
        set_motor_speed(motor2_in3, 0)
        set_motor_speed(motor2_in4, speed)
        time.sleep(0.1)
    stop_robot()


# Main loop
while True:
    distance = get_distance_from_pwm()

    if distance < 1000:  # If obstacle is within 1 meter
        stop_robot()
        turn_toward_obstacle()
        move_forward()
    else:
        # QRE1113 sensor logic
        if qre1113_sensor.value() == 0:  # Black surface
            stop_robot()
            time.sleep(0.5)
            turn_around()
        else:
            move_forward()

    time.sleep(0.1)
