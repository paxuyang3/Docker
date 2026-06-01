import json
import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 데이터를 저장할 JSON 파일 경로
DATA_FILE = "courses.json"

class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str

def load_courses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_courses(courses):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=2)

@app.get("/courses")
def get_all_courses():
    return load_courses()

@app.post("/courses")
def add_new_course(course: Course):
    courses = load_courses()
    new_course_dict = course.model_dump()
    courses.append(new_course_dict)
    save_courses(courses)
    return {"message": "수강기록이 성공적으로 추가되었습니다.", "data": new_course_dict}