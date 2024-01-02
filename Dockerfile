FROM        python:3.11.7-alpine3.18

WORKDIR     /usr/src/app

RUN         apk add build-base libffi-dev git vim

COPY        requirements.txt ./requirements.txt

RUN         pip install -r requirements.txt

COPY        ./ /usr/src/app
