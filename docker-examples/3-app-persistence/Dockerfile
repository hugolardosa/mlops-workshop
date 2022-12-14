FROM python:3.8-alpine

RUN mkdir /app
RUN mkdir /app/files

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app.py app.py

EXPOSE 5000

VOLUME /app/files

ENTRYPOINT ["python3", "app.py"]
