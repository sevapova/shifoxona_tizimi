from fastapi import FastAPI

app = FastAPI(title="Shifoxona boshqaruv tizimi")


@app.get("/")
def home():
    return {
        "message": "Shifoxona boshqaruv tizimiga xush kelibsiz!"
    }


@app.get("/bemorlar")
def get_patients():
    return {
        "bemorlar": []
    }