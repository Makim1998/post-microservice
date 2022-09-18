from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
import shutil

router = APIRouter()


@router.get("/images/{path}", tags=["image"])
async def get_image(path):
    return FileResponse('imgs/' + path)


@router.post("/images", tags=["image"])
async def create_file(file: UploadFile = File()):
    with open(f'imgs/{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
