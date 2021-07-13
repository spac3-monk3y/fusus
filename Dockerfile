ARG VARIANT="3.9"

FROM python:${VARIANT}-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG APP_DIR=/usr/src/app

RUN apt-get update && apt-get -y install \
    binutils \
    python3-dev \
    libproj-dev \
    build-essential \
    postgresql-client

WORKDIR ${APP_DIR}

COPY requirements.txt .
RUN pip --disable-pip-version-check --no-cache-dir install -r requirements.txt
COPY . .

EXPOSE 8000
RUN chmod +x *.sh
CMD ["bash", "run.sh"]
