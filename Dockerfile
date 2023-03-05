FROM python:3.10
WORKDIR /app

RUN pip install flask
COPY main.py /app

ENTRYPOINT ["python", "main.py"]
