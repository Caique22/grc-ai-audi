FROM --platform=amd64 python:3.11.6-slim

ENV APP_HOME /itau
WORKDIR $APP_HOME

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install with --no-cache-dir -r requirements.txt
RUN ls -la $APP_HOME
COPY ./main.py ./main.py
COPY ./utils ./utils
COPY ./grc ./grc

CMD ["uvicorn", "main:app"]
