FROM symbiot_lib_builder

COPY . /usr/src/symbiot_engine

WORKDIR /usr/src

RUN pip install requests

RUN mv symbiot_engine/run_engine.py .

EXPOSE 5001

CMD ["python", "run_engine.py", "--docker"]