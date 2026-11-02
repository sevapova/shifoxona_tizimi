from fastapi import APIRouter

router = APIRouter(
    prefix="/doctors",
    tags=["Shifokorlar"]
)

doctors = [
    {
        "id": 1,
        "full_name": "Aliyev Akmal",
        "specialty": "Kardiolog"
    },
    {
        "id": 2,
        "full_name": "Karimova Dilnoza",
        "specialty": "Nevropatolog"
    }
]


@router.get("/")
def get_doctors():
    return doctors