FROM python:latest

WORKDIR /usr/app/src

COPY random-iban-data.txt ./
COPY main.py ./

CMD [ "python", "./main.py"]