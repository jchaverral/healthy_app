FROM python:3.11

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

COPY src /opt/src

CMD ["python3", "/opt/src/main.py"]