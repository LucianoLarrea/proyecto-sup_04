FROM tiangolo/uvicorn-gunicorn-fastapi

COPY ./choco.py .
COPY ./choco.ipynb .