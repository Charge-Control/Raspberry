import pigpio
import time

TRIG = 21
ECHO = 20

pi = pigpio.pi()

if not pi.connected:
    exit()

pi.set_mode(TRIG, pigpio.OUTPUT)
pi.set_mode(ECHO, pigpio.INPUT)

print("초음파 거리 측정기")

pi.write(TRIG, 0)
print("초음파 출력 초기화")
time.sleep(2)

try:
    while True:
        pi.write(TRIG, 1)
        time.sleep(0.00001)  # 10uS의 펄스 발생을 위한 딜레이
        pi.write(TRIG, 0)

        start = time.time()
        while pi.read(ECHO) == 0:
            start = time.time()  # Echo 핀 상승 시간값 저장

        stop = time.time()
        while pi.read(ECHO) == 1:
            stop = time.time()  # Echo 핀 하강 시간값 저장

        check_time = stop - start
        distance = check_time * 34300 / 2
        print("Distance : %.1f cm" % distance)
        time.sleep(0.4)

except KeyboardInterrupt:
    print("거리 측정 완료")
    pi.stop()
