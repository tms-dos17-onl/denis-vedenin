FROM python:3.10

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt 
CMD [ "ls", "-la" ]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver"]