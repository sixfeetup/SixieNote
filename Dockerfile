FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/project

ARG DEVEL=no

RUN pip --no-cache-dir --disable-pip-version-check install --upgrade pip setuptools wheel

COPY requirements /tmp/requirements

RUN set -x \
    && if [ "$DEVEL" = "yes" ]; then pip --no-cache-dir --disable-pip-version-check install -r /tmp/requirements/dev.txt; fi

RUN set -x \
    && pip --no-cache-dir --disable-pip-version-check \
            install -r /tmp/requirements/main.txt \
                    $(if [ "$DEVEL" = "yes" ]; then echo '-r /tmp/requirements/tests.txt'; fi)
