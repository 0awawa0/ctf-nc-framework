FROM python:3-alpine

ARG TASK_NAME=main
ARG TASK_PORT=default
ENV TASK_NAME ${TASK_NAME}
ENV TASK_PORT ${TASK_PORT}
WORKDIR /chall
COPY . .
CMD ./ctfnc prod --port ${TASK_PORT} --task ${TASK_NAME}