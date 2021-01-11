FROM python:3-alpine

ARG TASK_NAME=main
ENV TASK_NAME ${TASK_NAME}
WORKDIR /chall
COPY . .
CMD ./ctfnc prod --port 13337 --task ${TASK_NAME}