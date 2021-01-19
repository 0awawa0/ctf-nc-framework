FROM python:3.8-slim

# For some tasks: RUN pip install --no-cache-dir pycryptodome

ARG TASK_NAME=main
ARG TASK_PORT=default
ENV TASK_NAME ${TASK_NAME}
ENV TASK_PORT ${TASK_PORT}
WORKDIR /chall
COPY . .
CMD ./ctfnc prod --port ${TASK_PORT} --task ${TASK_NAME}