from fastapi import APIRouter

router = APIRouter()

# Sample route for seat availability
@router.get("/seat_status/{study_area}")
async def get_seat_status(study_area: str):
    # For now, return dummy data
    return {
        "study_area": study_area,
        "total_seats": 50,
        "occupied_seats": 20,
        "available_seats": 30
    }
