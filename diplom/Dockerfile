FROM python:3.10

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt 
RUN sleep 60
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver"]