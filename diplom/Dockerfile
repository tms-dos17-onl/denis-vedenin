FROM python:3.10

WORKDIR .

COPY . ./

RUN pip install -r requirements.txt 
RUN sleep 30
RUN chmod +x runapp.sh

EXPOSE 8000
ENTRYPOINT ["/bin/bash", "runapp.sh"]
# CMD ["/bin/bash", "runapp.sh"]