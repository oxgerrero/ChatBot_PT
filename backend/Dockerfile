FROM python:3.11

WORKDIR /app

COPY . .
ENV PYTHONPATH=/app
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "python -m app.training.prepare_data && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
