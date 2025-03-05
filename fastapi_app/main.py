from fastapi import FastAPI

app = FastAPI()


@app.get("/info")
def get_info():
    return {
        "app_name": "Parcial",
        "code": "240220201006",
        "developer": "Juan Felipe Giraldo",
        "burden": "student",
        "framework": "FastAPI",
    }
