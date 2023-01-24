FROM python:3.11.1
MAINTAINER PerfectoZ
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD exec gunicorn profiles_project.wsgi:application --bind 0.0.0.0:8000 --workers 3