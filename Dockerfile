FROM python:3-alpine

ARG TASK_NAME=main
ENV TASK_NAME ${TASK_NAME}
WORKDIR /chall
COPY . .
CMD ./ctfnc prod --task ${TASK_NAME}