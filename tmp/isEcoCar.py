import requests
import json

#이미지에서 추출한 번호 넣기
car_number = "104호4670"
url = f"https://ev.or.kr/nportal/buySupprt/selectNonpolluCheck.ajax"

params = {
    'selectCarNum': '1',
    'searchWord': car_number
}

response = requests.post(url, params=params)

if response.status_code == 200:
    print("요청이 성공적으로 전송되었습니다.")
    data = response.json()["data"]
    car_type = data["CAR_TYPE_NM"]
    print("차량정보 : ", car_type)
    if car_type=="1종" or car_type=="2종" :
        isEcoCar = True
    else :
        isEcoCar = False
    print("isEcoCar : ", isEcoCar)

    
else:
    print("요청에 실패하였습니다. 상태 코드:", response.status_code)
