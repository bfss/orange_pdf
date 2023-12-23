# -*- coding: utf-8 -*-
from fastapi import FastAPI, UploadFile
from .pdf.router import router as pdf_router


app = FastAPI()

app.include_router(pdf_router)
