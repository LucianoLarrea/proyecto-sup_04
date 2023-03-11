FROM tiangolo/uvicorn-gunicorn-fastapi

RUN pip install pandas
RUN pip install polars

COPY ./app .


