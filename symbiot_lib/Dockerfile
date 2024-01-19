FROM python:3 AS symbiot_lib_builder

WORKDIR /usr/src/symbiot_lib

COPY . .

RUN pip install --no-cache-dir \
    setuptools selenium openai==0.28 injector flask