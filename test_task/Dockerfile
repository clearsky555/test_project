FROM python:3.10.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update \
    && apt-get install -y --no-install-recommends libpoppler-glib-dev libqhull-dev gdal-bin \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 1111

CMD ["python", "manage.py", "migrate"]

