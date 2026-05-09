from fastapi import FastAPI

app = FastAPI()

@app.get("/receive")
def read_message(msg: str = "No message"):
    print(f"터미널에 수신된 메시지: {msg}")
    return {"status": "success", "received_msg": msg}