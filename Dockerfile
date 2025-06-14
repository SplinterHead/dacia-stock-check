FROM python:3.13-alpine

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY *.py .

CMD ["python", "main.py"]