FROM python:3.7

ADD . ./app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8500

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8500"]