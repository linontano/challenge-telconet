# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /codetelco
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY ./src .
CMD ["flask","run"]
