from fastapi import APIRouter

router = APIRouter(prefix="/students", tags=["Students"])

@router.get("/")
def list_students():
    return {"students": []}

@router.get("/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id}
