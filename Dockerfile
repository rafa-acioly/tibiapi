FROM python:3.12.3-slim

WORKDIR /app

COPY . .

RUN pip install pipenv && pipenv install --system --deploy

EXPOSE 8080

CMD ["uvicorn", "tibiapi.main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "4"]
