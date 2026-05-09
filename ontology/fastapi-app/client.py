import requests

# 서버 주소와 보낼 메시지 설정
URL = "http://127.0.0.1:8000/receive"
params = {"msg": "안녕하세요! 클라이언트에서 보낸 메시지입니다."}

# GET 요청 보내기
response = requests.get(URL, params=params)

# 결과 확인
if response.status_code == 200:
    print("서버 응답:", response.json())
else:
    print("요청 실패:", response.status_code)