from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Services.ImagePredictionService import predict_troop_and_color, predict_json, predict_countries_map, predict_view_result, get_colors_image, predict_value_total, get_data_test
app = FastAPI()

origins = [
    "*"  # Outra variação do endereço do frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict/")
async def predict(image: UploadFile = File(...)):
    try:
        return await predict_json(image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict-countries/")
async def predict_countries(image: UploadFile = File(...)):
    try:
       return await predict_countries_map(image)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/predict-view/")
async def predict_view(image: UploadFile = File(...)):
    try:
        return await predict_view_result(image)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.post("/get-pixel-color/")
async def get_pixel_color(image: UploadFile = File(...)):
    try:
        return await get_colors_image(image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/get-data/")
async def get_data():
    try:
        return await get_data_test()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict-value/")
async def predict_value(image: UploadFile = File(...)):
    try:
        return await predict_value_total(image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/predict-complete/")
async def predict_complete(image: UploadFile = File(...)):
    try:
        return await predict_troop_and_color(image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


