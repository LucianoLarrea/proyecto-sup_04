FROM tiangolo/uvicorn-gunicorn-fastapi

RUN pip3 install pandas


COPY ./app .


