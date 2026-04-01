FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install django gunicorn psycopg2-binary
CMD ["gunicorn","demoapp.wsgi:application","--bind","0.0.0.0:8000"]
