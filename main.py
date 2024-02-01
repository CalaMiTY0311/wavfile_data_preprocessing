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
import subprocess

from audio_processor.setting_dataset import data_processing
from audio_processor.setting_mr import mr

current_directory = os.path.dirname(os.path.abspath(__file__))

# ff_path를 포함한 전체 경로
ff_path = os.path.join(current_directory, "ff_path")

# 환경 변수에 현재 디렉토리의 ff_path 추가
os.environ["PATH"] = f'{os.environ["PATH"]};{ff_path}'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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


async def make_mr(file: UploadFile):
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    separation = mr('audio_processor/mr',id, 2)
    zip_path = separation.separating(file)
    return zip_path

@app.post("/make_mr/")
async def song_mr(file: UploadFile = File(...)):
    zip_path = await make_mr(file)
    return FileResponse(zip_path, filename='output.zip', media_type="application/zip")





















@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__=='__main__': 
    uvicorn.run(app, host='0.0.0.0', port = 8000)
