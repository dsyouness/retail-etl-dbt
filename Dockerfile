FROM ghcr.io/dbt-labs/dbt-bigquery:1.4.latest

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
