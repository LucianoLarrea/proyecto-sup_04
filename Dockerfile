FROM tiangolo/uvicorn-gunicorn-fastapi

RUN pip install pandas

COPY ./choco.py .

COPY ./choco.ipynb .
