FROM python:3.11-slim

LABEL authors="ayesha"

WORKDIR /main

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /main

EXPOSE 8501

CMD ["python","backend.py"]

ENTRYPOINT ["streamlit","run","frontend.py"]