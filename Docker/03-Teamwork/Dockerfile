# INSTRUCTION arguments

FROM python:3.10.8-slim-bullseye
WORKDIR /code

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
