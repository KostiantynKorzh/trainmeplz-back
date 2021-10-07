FROM python:3.9-slim-buster

COPY . /source

WORKDIR /source

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

WORKDIR /source/src/back

ENV FLASK_APP=run.py
ENV PYTHONPATH=/source/

ENTRYPOINT ["flask"]

CMD ["run", "--host=0.0.0.0"]