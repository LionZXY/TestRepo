FROM python:3-alpine

WORKDIR /tg/

RUN pip install python-telegram-bot

COPY send_message.py /tg/send_message.py

ENTRYPOINT ["/tg/send_message.py"]
