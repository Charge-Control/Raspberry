import serial
import sys
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time

def sensor():
    FromArduino = serial.Serial("/dev/ttyACM0" , 9600)   #통신포트 open
    FromArduino.flushInput()
    GPIO.cleanup() # cleanup all GPIO 
    while True:
        light = int(FromArduino.readline())
        
        if light < 160:      #자동차가 출입했을 때
            print("자동차가 출입했습니다")
            
            GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
            GPIO.setup(26, GPIO.OUT) # output rf
            GPIO.output(26, GPIO.HIGH)
            
            camera = PiCamera()
            camera.start_preview()
            camera.rotation = 180      #180도 회전
            sleep(1)    #번호판사진을 찍는데 걸리는 시간
            camera.capture("/home/pi/CarLicensePlate/test_img/pic.jpg")   #사진 저장 경로
            camera.stop_preview()
            camera.close()
            
            GPIO.cleanup() # 부저 끄기
            
            sleep(1)
            print("번호판 인식으로 넘어갑니다")
            import imgprocess2    #조도센서인식후 바로 번호판인식
            imgprocess2.computervision()
            
            sys.exit(1)
        else:                #아무것도 없을 때
            print("현재 아무것도 들어오지 않았습니다")
            sleep(1)
            continue
        
sensor()