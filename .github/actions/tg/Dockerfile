FROM python:3-alpine

RUN pip install python-telegram-bot

COPY send_message.py send_message.py

ENTRYPOINT ["python", "send_message.py"]
