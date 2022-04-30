FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir app \
    && chmod -R 777 /app

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

#RUN useradd -u 1234 pythonuser
#USER pythonuser

COPY . /app/
