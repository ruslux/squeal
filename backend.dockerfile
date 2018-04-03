FROM python:3.6

COPY ./requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt
WORKDIR /var/www


