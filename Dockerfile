FROM python:3.11.3-slim-bullseye


WORKDIR /app


COPY requirements.txt .


RUN python -m pip install -r requirements.txt


COPY . /app

RUN chmod +x run.sh

CMD ["sh", "run.sh"]