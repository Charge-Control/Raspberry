def computervision():
    
    #최종 번호판 추출 함수
    parking_classfication("/home/pi/CarLicensePlate/test_img/pic.jpg")  #인식을 하려는 사진 (경로 수정가능)
    os.remove("/home/pi/CarLicensePlate/test_img/pic.jpg")   #찍힌 사진 삭제
    
    sleep(3)
    import serialmicro    #번호판 인식후 QRcode를 인식하기 위해 초음파센서
    serialmicro.micro()    #초음파로 인식 시작
        
    sys.exit(1)  #메모리 과부하를 막기 위한 exit()
    
computervision()