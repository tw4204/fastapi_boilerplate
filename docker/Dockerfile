FROM python:3.8.2
RUN apt-get clean && apt-get update && apt-get install -y \
  libpq-dev \
  postgresql \
  postgresql-contrib
RUN mkdir /install
COPY source/requirements.txt /install
WORKDIR /install
RUN pip install -r requirements.txt
