FROM python:3.11-alpine

WORKDIR /opt/app

COPY src/ /opt/app/

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "app.py"]