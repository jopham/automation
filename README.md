# Automation
Mini automation project


## Architecture
- main.py script orchestrates the flow of the automation.
- commonScripts folder contains functions that can be re-used in different parts of the automation.

## What it does right now
- Creates folder structure for logs
- Opens the main log and writes to it

## To do
- Get and pre-process data if necessary
- Create/pick existing ML model to run
- commonScripts:
  - getCall: create a GET call
  - postCall: create a POST call
  - uploadToS3: upload data/results to S3
- Add a scheduler (options: crontab, schedule)
