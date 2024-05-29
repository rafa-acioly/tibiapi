FROM python:3.12.3-slim

WORKDIR /app

COPY . .

RUN pip install pipenv && pipenv install --deploy

RUN pipenv run python -m pip freeze > /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8080

CMD ["uvicorn", "tibiapi.main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "4"]
