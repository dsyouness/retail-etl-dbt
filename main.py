import logging

from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/run")
def run_dbt():
    # Run the dbt run command and capture the output
    result = subprocess.run(["dbt", "run"], capture_output=True, text=True)

    # Return the output as a response
    return {"output": result.stdout, "error": result.stderr}

@app.get("/docs")
def expose_docs():
    # log the output of the command
    result = subprocess.run(["dbt", "docs", "generate"], capture_output=True, text=True)
    logging.info(result.stdout)
    result = subprocess.run(["dbt", "docs", "serve"], capture_output=True, text=True)
    logging.info(result.stdout)

    return {"output": result.stdout, "error": result.stderr}