FROM python:3.10

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt 
RUN sleep 60
RUN chmod +x runapp.sh

EXPOSE 8000

CMD ["/bin/bash", "runapp.sh"]