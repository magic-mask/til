# FaskAPI로 Ontology 구현 해보기

Ontology구현에 앞서 간단한 RDB(Relational Database)를 먼저 구현해봅니다

## 환경설정

```bash
uv add fastapi uvicorn
```

## 서버 실행

### main.py

```python
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "query": q}
```

```bash
uvicorn main:app --reload
```

## server-client 구현

### server.py

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/receive")
def read_message(msg: str = "No message"):
    print(f"터미널에 수신된 메시지: {msg}")
    return {"status": "success", "received_msg": msg}
```

### client.py

```python
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
```

### Step 1 : 서버 실행(첫 번째 터미널)

서버를 먼저 띄워서 클라이언트의 요청 대기

```bash
uvicorn server:app --reload
```

### Step 2 : 클라이언트 실행 (두 번째 터미널)

새 터미널 창을 열고 클라이언트 파일을 실행하여 메시지 전송

```bash
python client.py
```

![Figure](../../imgs/RDB-flowchart.png)