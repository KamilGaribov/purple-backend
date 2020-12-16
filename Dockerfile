FROM python:3
ENV PYTHONUNBUFFERED 1
RUN adduser -D dockuser
USER dockuser
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
EXPOSE 8000
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /code/
CMD ["python3", "manage.py", "runserver"]



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