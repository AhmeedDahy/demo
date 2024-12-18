from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/submit/")
async def submit_form(
    age: int = Form(...),
    height: float = Form(...),
    weight: float = Form(...),
    bodyFatPercentage: float = Form(...),
    gender: str = Form(...),
    activity: str = Form(...),
    weightPlan: str = Form(...),
    mealPerDay: int = Form(...),
    dietDuration: str = Form(...),
):
    return JSONResponse(content={
        "message": "Form received successfully",
        "data": {
            "age": age,
            "height": height,
            "weight": weight,
            "bodyFatPercentage": bodyFatPercentage,
            "gender": gender,
            "activity": activity,
            "weightPlan": weightPlan,
            "mealPerDay": mealPerDay,
            "dietDuration": dietDuration,
        }
    })
