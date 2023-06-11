from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.main import prediction
# import uvicorn

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:5500/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello! Location, Area, Bed, Bath are the parameters. Go to /prediction and get prediction of rental price. There're list of cities in a secret file :3."}

@app.get("/prediction")
async def get_prediction(location: str, area: str, bed: str, bath: str):
    print(location, int(area), int(bed), int(bath))
    content = prediction(location, int(area), int(bed), int(bath))

    # if content['status'] == False:
    #     raise HTTPException(status_code=404, detail=content['msg'])

    return { 'status_code': 200, 'content': content }

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")