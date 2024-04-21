from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/run")
def run_dbt():
    # Run the dbt run command and capture the output
    result = subprocess.run(["dbt", "run"], capture_output=True, text=True)

    # Return the output as a response
    return {"output": result.stdout, "error": result.stderr}
