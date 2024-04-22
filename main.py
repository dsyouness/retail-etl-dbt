import logging

from fastapi import FastAPI
import subprocess

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

@app.get("/run")
def run_dbt():
    logger.info("Running dbt run command")
    # Run the dbt run command and capture the output
    result = subprocess.run(["dbt", "run"], capture_output=True, text=True)

    # Write the output to the logs
    logger.info("dbt run output: " + result.stdout)
    logger.info("dbt run error: " + result.stderr)

    # Return the output as a response
    return {"output": result.stdout, "error": result.stderr}
