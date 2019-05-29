import os
import RPi.GPIO as GPIO
import time


class motors(object):
    """
    Control class for DC motor and Servo motors
    That class use BOARD mode for control gpio pins
    ...

    Atributes
    ---------
    forward_pin : int
        forward movement  
    backward_pin : int
        backward movement
    servo_pin : int
        control servo motor

    servo_center : float
        Servo center position, relative position needs to calibrate
    servo_left : float
        Servo left position, relative position needs to calibrate
    servo_Right : float
        Servo Right position, relative position needs to calibrate
    Methods
    -------

    """

    def __init__(self, **kwargs):
        """ 
        Parameters
        ----------

        """
        GPIO.cleanup()
        self.forward_pin = kwargs['forward_pin']
        self.backward_pin = kwargs['backward_pin']
        self.servo = kwargs['servo_pin']

        self.servo_center = 4.6
        self.servo_left = 3.2
        self.servo_right = 6

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.forward_pin, GPIO.OUT)  #
        GPIO.setup(self.backward_pin, GPIO.OUT)  #
        GPIO.setup(self.servo,GPIO.OUT) 

        self.p = GPIO.PWM(self.servo,50)
        self.p.start(self.s)  
        self.p.ChangeDutyCycle(5) 
        time.sleep(1)

        print("Engines connected!")

    def ahead(self):
        GPIO.output(self.backward_pin,False)
        GPIO.output(self.forward_pin,True)


    def backward(self):
        GPIO.output(self.backward_pin,True)
        GPIO.output(self.forward_pin,False)


    def stop(self):
        GPIO.output(self.backward_pin,False)
        GPIO.output(self.forward_pin,False)


    def turn_right(self):
        self.p.ChangeDutyCycle(self.servo_right)


    def turn_left(self):
        self.p.ChangeDutyCycle(self.servo_left) 


    def reset_servo(self):
        self.p.ChangeDutyCycle(4.6)


    def gpio_cleanup(self): 
        GPIO.cleanup()  
    
    # def f_direita(self):
    #     self.p.ChangeDutyCycle(self.servo_right)
    #     GPIO.output(self.backward_pin,False)
    #     GPIO.output(self.forward_pin,True)

    # def t_direita(self):
    #     self.p.ChangeDutyCycle(self.servo_right)
    #     GPIO.output(self.backward_pin,True)
    #     GPIO.output(self.forward_pin,False)

    # def f_esquerda(self):
    #     self.p.ChangeDutyCycle(self.servo_left) 
    #     GPIO.output(self.backward_pin,False)
    #     GPIO.output(self.forward_pin,True)

    # def t_esquerda(self):
    #     self.p.ChangeDutyCycle(self.servo_left) 
    #     GPIO.output(self.backward_pin,True)
    #     GPIO.output(self.forward_pin,False)

