FROM tiangolo/uvicorn-gunicorn-fastapi

RUN pip install pandas

COPY ./app .

COPY ./choco.ipynb .
