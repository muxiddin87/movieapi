FROM python:3.10.5

WORKDIR /netflix_

COPY . .

RUN pip3 install -r requirements.txt 

RUN chmod +x ./entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
