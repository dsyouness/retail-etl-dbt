FROM ghcr.io/dbt-labs/dbt-bigquery:1.4.latest

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8080

CMD ["run"]
