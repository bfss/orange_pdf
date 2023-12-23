# -*- coding: utf-8 -*-
import os
import shutil
import uuid
from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
from pypdf import PdfWriter


router = APIRouter(prefix="/pdf")

@router.post("/merge/")
async def pdf_merge(files: list[UploadFile]):
    uid = uuid.uuid4().hex
    pdf_dir = os.path.join("upload_pdfs", uid)
    pdf_out = os.path.join(pdf_dir, '结果.pdf')
    os.makedirs(pdf_dir)
    with PdfWriter() as merger:
        for file in files:
            pdf = os.path.join(pdf_dir, file.filename)
            with open(pdf, 'wb') as f:
                shutil.copyfileobj(file.file, f)
            merger.append(pdf)
        merger.write(pdf_out)
    return FileResponse(pdf_out, media_type='application/octet-stream', filename="结果.pdf")
