# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install -y cron nodejs

COPY stu_id.txt /mnt/stu_id.txt

COPY hello-cron /etc/cron.d/hello-cron
RUN chmod 0644 /etc/cron.d/hello-cron &&\
    crontab /etc/cron.d/hello-cron
RUN touch /var/log/cron.log

COPY . .

CMD cron && tail -f /var/log/cron.log

