# 1-get

# Напишите HTTP-запрос, который выполняет GET запрос на адрес "/index" с использованием HTTP/1.0.
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/index")
async def read_index():
    return {"message": "index-ке қош келдіңіз"}

# 2-post

# Напишите HTTP-запрос, который выполняет POST запрос на
# адрес "/api/login" с заголовком "Content-Type:
# application/x-www-form-urlencoded". В теле запроса отправьте
# "username=Alice&password=secret". Используйте метод HTTP/1.0.
# Подсчитайте и включите в запрос заголовок "Content-Length".

@app.post("/api/login")
async def login(username: str, password: str):
    return {"username": username, "password": password}

# 3-get-1.1

# Напишите HTTP-запрос, который выполняет GET запрос на адрес "http://example.com/home" с использованием HTTP/1.1.
@app.get("/home")
async def read_home():
    return {"message": "home-ге қош келдіңіз"}

# 4-get-1.1-accept

# Напишите HTTP-запрос, который выполняет GET запрос на адрес "http://example.com/data" и
# отправляет заголовок "Accept: application/json" с использованием HTTP/1.1.
@app.get("/data")
async def get_data():
    response_data = {"message": "data"}
    return JSONResponse(content=response_data)

# 5-post-1.1-body

# Напишите HTTP-запрос, который выполняет POST запрос на адрес "http://example.com/api/messages"
# с заголовком "Content-Type: application/json".
#
# В теле запроса отправьте `{"username": "Alice", "msg": "Hello"}`.
#
# Используйте метод HTTP/1.1. Подсчитайте и включите в запрос заголовок "Content-Length".
@app.get("/api/messages")
async def api_message(username: str, msg: str):
    response_data = {"username": username, "msg": msg}
    return JSONResponse(content=response_data)

# 6-put-1.1-body

# Напишите HTTP-запрос, который выполняет PUT запрос на адрес "http://example.com/api/messages/42"
# с заголовком "Content-Type: text/plain".
#
# В теле запроса отправьте `Updated message`.
#
# Используйте метод HTTP/1.1. Подсчитайте и включите в запрос заголовок "Content-Length".
@app.put("/api/messages/{message_id}")
async def update_message(message_id: int, request: Request):
    body = await request.body()
    body_text = body.decode('utf-8')  # Преобразуем байты в строку
    return {"message_id": message_id, "updated_message": body_text}

## 7-delete-1.1

# Напишите HTTP-запрос, который выполняет DELETE запрос на адрес "http://example.com/api/messages/42".
#
# Используйте метод HTTP/1.1.
@app.delete("/api/messages/{message_id}")
async def delete_message(message_id: int):
    return {"message": f"{message_id} - номерлі id өшірілді"}