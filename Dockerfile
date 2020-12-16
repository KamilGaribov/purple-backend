FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
EXPOSE 8000
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /code/
RUN apt-get update && apt-get install -y \
  locales \
  locales-all \
  build-essential \
  libpq-dev \
  libjpeg-dev \
  binutils \
  libproj-dev \
  gdal-bin \
  libxml2-dev \
  libxslt1-dev \
# FROM python:3
# ENV PYTHONUNBUFFERED 1
# RUN adduser -D dockuser
# USER dockuser
# RUN mkdir /code
# WORKDIR /code
# COPY requirements.txt /code/
# EXPOSE 8000
# RUN pip3 install --upgrade pip
# RUN pip3 install -r requirements.txt
# COPY . /code/
# CMD ["python3", "manage.py", "runserver"]



# FROM python:3
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# WORKDIR /code
# COPY requirements.txt /code/
# EXPOSE 8000
# RUN pip3 install --upgrade pip
# RUN pip3 install -r requirements.txt
# COPY . /code/
# CMD ["python3", "manage.py", "makemigrations", "&&", "python3", "manage.py", "migrate", "&&", "python3", "manage.py", "runserver"]