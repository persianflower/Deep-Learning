
FROM python:3.11-slim

WORKDIR /main

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /main

EXPOSE 8000

CMD ["python","main.py"]