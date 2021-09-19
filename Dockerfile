FROM python:3.8-slim-buster

COPY . /src

WORKDIR /src

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

WORKDIR /src/app/back

ENV FLASK_APP=__init__.py

ENTRYPOINT ["flask"]

CMD ["run", "--host=0.0.0.0"]