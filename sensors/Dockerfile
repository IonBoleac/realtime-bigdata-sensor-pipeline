FROM python:3.8-slim-buster

RUN apt update
RUN apt install curl -y

RUN curl -L https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh > /usr/bin/wait-for-it && \
    chmod +x /usr/bin/wait-for-it

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py .

CMD ["/bin/bash", "-c", "wait-for-it mosquitto:1883 && python -u simulate.py 5"]