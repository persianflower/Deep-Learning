
FROM python:3.11-slim

WORKDIR /main

COPY . /main

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python","main.py"]