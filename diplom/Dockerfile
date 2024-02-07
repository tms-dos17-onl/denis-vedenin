FROM python:3.10

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt 
RUN sleep 30
RUN chmod +x runapp.sh

EXPOSE 8000
ENTRYPOINT ["/bin/bash", "runapp.sh"]
# CMD ["/bin/bash", "runapp.sh"]