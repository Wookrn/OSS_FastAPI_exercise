from fastapi import FastAPI
from course_records import course_records_router
import uvicorn

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Course Records"}

app.include_router(course_records_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)