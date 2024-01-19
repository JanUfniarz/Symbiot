FROM symbiot_lib_builder

COPY . /usr/src/symbiot_server

WORKDIR /usr/src

RUN pip install psycopg2 flask_sqlalchemy

RUN mv symbiot_server/run_server.py .

EXPOSE 5000

CMD ["python", "run_server.py", "--docker"]
