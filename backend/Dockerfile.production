FROM debian:11
WORKDIR /app

# Get python, pip
RUN apt-get update -y
RUN apt-get install python3 python3-pip -y

# Install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Run application
COPY . .
EXPOSE 8000
ENTRYPOINT gunicorn --bind=0.0.0.0:8000 src.api:app