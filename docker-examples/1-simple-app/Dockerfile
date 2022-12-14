FROM python:3.8-alpine

RUN mkdir /app

WORKDIR /app

COPY app.py app.py

# python3 -u app.py
# force the stdout and stderr streams to be unbuffered
# so that they are printed as soon as they are produced
ENTRYPOINT ["python3", "-u" ,"app.py"]
