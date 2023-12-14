import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
Forward_motor =31
Backward_motor=32
RIght_motor=33
Left_motor=35
#vertical_motor_en=36
#Horizantal_motor_en=37

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Forward_motor,GPIO.OUT)
GPIO.setup(Backward_motor,GPIO.OUT)
GPIO.setup(RIght_motor,GPIO.OUT)
GPIO.setup(Left_motor,GPIO.OUT)

#GPIO.setup(vertical_motor_en,GPIO.OUT)
#GPIO.setup(Horizantal_motor_en,GPIO.OUT)

#pwm_h = GPIO.PWM(vertical_motor_en , 1000)
#pwm_v = GPIO.PWM(Horizantal_motor_en , 1000)

#pwm_h.start(25)
#pwm_v.start(25)

def forward(second):
    print("Forward")
    GPIO.output(Forward_motor,GPIO.HIGH)
    GPIO.output(Backward_motor,GPIO.LOW)
    GPIO.output(RIght_motor,GPIO.LOW)
    GPIO.output(Left_motor,GPIO.LOW)
    time.sleep(second)

def reverse(second):
    print("reverse")
    GPIO.output(Forward_motor,GPIO.LOW)
    GPIO.output(Backward_motor,GPIO.HIGH)
    GPIO.output(RIght_motor,GPIO.LOW)
    GPIO.output(Left_motor,GPIO.LOW)
    time.sleep(second)

def left(second):
    print("left")
    GPIO.output(Forward_motor,GPIO.LOW)
    GPIO.output(Backward_motor,GPIO.LOW)
    GPIO.output(RIght_motor,GPIO.LOW)
    GPIO.output(Left_motor,GPIO.HIGH)
    time.sleep(second)

def right(second):
    print("right")
    GPIO.output(Forward_motor,GPIO.LOW)
    GPIO.output(Backward_motor,GPIO.LOW)
    GPIO.output(RIght_motor,GPIO.HIGH)
    GPIO.output(Left_motor,GPIO.LOW)            
    time.sleep(second)

def stop():
    print("stop")   

def exit_():
    GPIO.cleanup()

def main():
    forward(2)
    reverse(2)
    left(2)
    right(2)
    stop()
    exit_()



if __name__ == '__main__':
    main()