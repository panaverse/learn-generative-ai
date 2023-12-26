FROM python:3.12

WORKDIR /travel_ai_service

COPY ./requirements.txt /travel_ai_service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /travel_ai_service/requirements.txt

COPY ./app /travel_ai_service/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
