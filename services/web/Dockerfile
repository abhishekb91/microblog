FROM python:3.8.0-alpine

RUN adduser -D microblog

WORKDIR /home/microblog

# install psycopg2 dependencies, and bash to connect to app sever if needed
RUN apk update
RUN apk add bash postgresql-dev gcc python3-dev musl-dev

# copy project
COPY . ./
RUN chmod +x boot.sh

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chown -R microblog:microblog ./
USER microblog

ENTRYPOINT ["./boot.sh"]