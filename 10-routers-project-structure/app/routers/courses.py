from fastapi import APIRouter

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("/")
def list_courses():
    return {"courses": []}

@router.get("/{course_id}")
def get_course(course_id: int):
    return {"course_id": course_id}
