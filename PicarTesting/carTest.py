from picar import PiCar, test
import RPi.GPIO as GPIO
import time


motor_pin1 = 37
motor_pin2 = 38
motor_enable = 12
servo_nod = 13
servo_swivel = 18
servo_steer = 15
ultrasonic_trigger = 16
ultrasonic_echo = 17
# ground in 9
pin_conf = (motor_enable, motor_pin1, motor_pin2, servo_nod, servo_swivel, servo_steer, ultrasonic_trigger, ultrasonic_echo)
car = PiCar(mock_car=True)

print(car)

car.set_motor(float(25))
time.sleep(5)
print(car)

#car.set_motor(str(25))
time.sleep(2)

print(car)

car.set_motor(75)
time.sleep(2)

print(car)
#test.execute_test(car)
car.stop()
GPIO.cleanup()
