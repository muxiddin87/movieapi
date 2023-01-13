FROM python:3.11

WORKDIR /app

COPY . /app/

RUN pip install requirements.txt

ENTRYPOINT ["python","app.py"]