FROM debian:11
WORKDIR /app

RUN apt-get update -y
RUN apt-get install python3 python3-pip -y

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT gunicorn --bind=0.0.0.0:8000 src.api:app