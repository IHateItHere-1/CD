FROM python:3-alpine

WORKDIR /app

#depends
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
    
RUN pip install --user mysql-connector
RUN pip install flask
RUN pip install pyopenssl
RUN pip install waitress 

# Bundle app source
COPY . .

EXPOSE 80
EXPOSE 443
CMD [ "python", "app.py" ]
#CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
