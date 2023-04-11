FROM        python:3.10.5-alpine3.16

WORKDIR     /usr/src/app

RUN         apk add build-base libffi-dev git vim

COPY        requirements.txt ./requirements.txt

RUN         pip install -r requirements.txt

COPY        ./ /usr/src/app
