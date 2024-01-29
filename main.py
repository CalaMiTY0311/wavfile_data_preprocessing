#export PATH=$PATH:/c/Users/axels/OneDrive/바탕\ 화면/translation_AI/ffmpeg-6.1.1-full_build/bin
#export PATH=$PATH:/c/Users/axels/OneDrive/바탕\ 화면/translation_AI/ff_path

from fastapi import FastAPI, File, UploadFile, HTTPException, background
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import aiofiles
import shutil
import os
import random, string

from audio_processor.setting_dataset import data_processing

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 사용 시에는 특정 origin을 지정하는 것이 좋습니다.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def make_dataset(file: UploadFile):
    wav_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    processor = data_processing('audio_processor/dataset', 15, wav_id)
    zip_path = processor.processing(file)

    return zip_path

@app.post("/make_dataset/")
async def processing(file: UploadFile = File(...)):
    path = await make_dataset(file)
    return FileResponse(path, filename="dataset.zip", media_type="application/zip")

# async def make_separation(file: UploadFile):
    





















@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__=='__main__': 
    uvicorn.run(app, host='0.0.0.0', port = 8000)
