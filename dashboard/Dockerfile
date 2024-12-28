FROM python:3.11

COPY requirements.txt /api/requirements.txt
RUN pip install -r /api/requirements.txt

COPY . .

CMD ["python", "/src/main.py"]