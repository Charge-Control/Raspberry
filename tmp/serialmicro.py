import serial
import sys
from time import sleep
import os
import RPi.GPIO as GPIO
import time
from picamera import PiCamera

def micro():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    while True:
        ser = serial.Serial('/dev/ttyUSB0',9600)   #while문이 계속 돌면서 통신포트 open
        microresult = int(ser.readline())
        
        GPIO.output(17, True)  #주차중인 경우 계속 LED가 깜박이도록한다. 
        time.sleep(0.1)
        GPIO.output(17, False)
        time.sleep(0.1)
        
        if microresult < 10:  #주차완료
            print("차가 주차완료했습니다 ")
            GPIO.output(17, False)
            
            camera = PiCamera()
            camera.start_preview()
            sleep(1)
            camera.rotation = 180      #180도 회전
            sleep(1)     #7초동안 QRcode 사진찍기
            camera.capture("/home/pi/qrcode/qrpic.jpg")   #qrcode사진 저장 경로
            camera.stop_preview()
            camera.close()
            
            print("QRcode 인식으로 넘어갑니다")
            import qrprocess       #사진찍고 QRcode 인식
            qrprocess.qr()
    
            sys.exit(1)    #이건 필수로 있어야 함
        elif microresult >= 10 and microresult < 90:   #주차중
            print("차가 주차중입니다")    
            continue
        else:                             #차가 다시 뒤로 나가면 조도센서로 처음부터 다시 인식
            print("차가 나갔습니다")
            GPIO.output(17, False)
            import serialard
            serialard.sensor()
            sys.exit(1)   #이것도 필수
            
micro()