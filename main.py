import logging

from fastapi import FastAPI,HTTPException
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

    # Check the return code of the command
    if result.returncode == 0:
        # The command succeeded, return a 200 status code and the output
        logger.info("dbt run command succeeded")
        logger.info("dbt run output: " + result.stdout)
        logger.info("dbt run error: " + result.stderr)

        return {"output": result.stdout, "error": result.stderr}
    else:
        # The command failed, raise an HTTPException with a 500 status code and the error message
        error_message = f"dbt run command failed with error: {result.stderr}"
        logger.error(error_message)
        raise HTTPException(status_code=500, detail=error_message)