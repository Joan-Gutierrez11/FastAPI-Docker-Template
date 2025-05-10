FROM python:3.12.10-alpine

WORKDIR /app

# Install dependencies
RUN apk update
RUN apk add bash \
    && apk add --virtual build-deps gcc musl-dev \
    && apk add --no-cache mariadb-dev

COPY ./requeriments.txt /app/requeriments.txt

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requeriments.txt

COPY . /app/
