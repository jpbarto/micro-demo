FROM python:3.11-alpine

WORKDIR /opt/app

COPY src/ /opt/app/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "app.py"]