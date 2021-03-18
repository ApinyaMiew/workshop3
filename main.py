from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from typing import Dict, Optional, List, Tuple
import uvicorn

app = FastAPI()

# httpsmethod [ get, post, put, patch, delete ]
# command database [ find, insert, update, delete]


@app.get("/")
def index():
    return JSONResponse(content={"message": "Hello,  World"}, status_code=200)


@app.get("/example/")
def get_query_parameter(
    start: int = 0, limit: int = 0, name: str = ""
):  # query_parameter คือ ตั้งแต่?เอาไว้sert ไปหน้าต่างๆ เช่น shoppy

    print("---> start", start)
    print("---> limit", limit)
    print("---> name", name)

    # response = {"message": f"start: {start} limit: {limit} name: {name}"}

    return JSONResponse(
        content={"message": f"start: {start} limit: {limit} name: {name}"},
        status_code=200,
    )


@app.get("/profile/{name}/{age}")
def get_path_parameter(name: str, age: int):
    return JSONResponse(
        content={"message": f"My name is: {name} age: {age}"},
        status_code=200,
    )


@app.get("/books")
def get_books():
    books = [
        {
            "book_id": 1,
            "book_name": "Harry Potter and Philosopher's Stone",
            "page": 223,
        },
        {
            "book_id": 2,
            "book_name": "Harry Potter and the Chamber of Secrets",
            "page": 251,
        },
        {
            "book_id": 3,
            "book_name": "Harry Potter and Pridoner of Azkaban",
            "page": 251,
        },
    ]

    return JSONResponse(content={"status": "ok", "data": dict__books}, status_code=200)

@app.get("/books/{book_id}")
def get_books_by_id(book_id: int):
    dict_books = {
            "book_id": 1,
            "book_name": "Harry Potter and Philosopher's Stone",
            "page": 223,
        }

        response = {"status": "ok", "data": book}
        return JSONResponse(content=response, status_code=200)

class createBookPayload(BaseModel): #BaseModel = การกำหนดค่าให้เป็นพื้นฐานในการกรอกข้อมูล
    id : str
    name: str
    page: int

#payload = body
@app.post("/books")
def create_books(req_body: createBookPayload):
    req_body_dict = req_body.dict()
    id = req_body_dict["id"]
    name = req_body_dict["name"]
    page = req_body_dict["page"]
    title = req_body_dict["title"]

    print("id", req_body_dict["id"])
    print("name", req_body_dict["name"])
    print("page", req_body_dict["page"])
    print("tital", req_body_dict["tital"])

    book = {
        "id": id,
        "name": name,
        "page": page,
        "tital": tital
    }
    response = {"status": "ok", "message": "ได้ค่ะ เดี๋ยวหนูจัดการเพิ่ม books ให้นะคะ", "data": book,}
    return JSONResponse(content=response, status_code=201)

class updateBookPayload(BaseModel):
    name: str
    page: int

@app.patch("/books/{book_id}")
def update_book_by_id(req_body: updateBookPayload, book_id: str):
    
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)