FROM python:3.10.6 AS BASE

WORKDIR /app

ADD . /app/
ADD ./intent-classification /app/

RUN pip install -r intent-classification/requirements.txt

RUN python -m spacy download en_core_web_sm
