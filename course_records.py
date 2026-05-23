from fastapi import APIRouter, HTTPException
from model import Course
import json

course_records_router = APIRouter()

JSON_FILE = "courses.json"

course_records_list = []

#json 파일에 post로 추가 작성하기
@course_records_router.post("/course_records")
async def create_course_record(course_records: Course) -> dict:
    try:
        #json 파일 읽어오기
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            course_records_list = json.load(f)

        #읽어온 리스트에 새로운 record append
        course_records_list.append(course_records.model_dump())

        #json 파일에 리스트 추가해서 저장
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(course_records_list, f, ensure_ascii=False, indent=4)
        return {"message": "Course record created successfully"}
    except Exception as e:
        print(f"잘못된 형식 입력: {e}")
        raise HTTPException(status_code=500, detail="Invalid input format")

#json 파일 읽어오기
@course_records_router.get("/course_records")
async def get_course_records() -> dict:
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        course_records_list = json.load(f)
    return {"course_records": course_records_list}