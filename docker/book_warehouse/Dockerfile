# Dockerfile book_warehouse

FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY book_warehouse/requirements.txt /
RUN pip install -r requirements.txt

WORKDIR /usr/app

COPY book_warehouse /usr/app


COPY ./docker-entrypoint.sh /usr/docker-entrypoint.sh
RUN chmod +x /usr/docker-entrypoint.sh
ENTRYPOINT [ "/usr/docker-entrypoint.sh" ]


