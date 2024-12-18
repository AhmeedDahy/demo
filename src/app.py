from fastapi import FastAPI,Form
from fastapi.responses import JSONResponse
app = FastAPI(
  title='RAG API',
  description='A simple app',
  version='0.1'
)


@app.post("/submit/")
async def submit_form(
    age: int,
    height: float,
    weight: float,
    bodyFatPercentage: float,
    gender:str,
    activity:str,
    weightPlan:str,
    mealPerDay:int,
    dietDuration:str,
):

    return JSONResponse( content={
        "message": "Form received successfully",
        "data": {
          'age': age,
          'height': height,
          'weight': weight,
          'bodyFatPercentage': bodyFatPercentage,
          'gender':gender,
          'activity':activity,
          'weightPlan':weightPlan,
          'mealPerDay':mealPerDay,
          'dietDuration':dietDuration,
        }
    },status_code=200)
