FROM symbiot_lib_builder

COPY . /usr/src/symbiot_core

WORKDIR /usr/src

RUN pip install requests

RUN mv symbiot_core/run_core.py .

EXPOSE 5001

CMD ["python", "run_core.py"]