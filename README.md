# ETL Airflow Retail Pipeline

This project demonstrates a simple ETL pipeline using Apache Airflow for a hypothetical retail data workflow.
It extracts data from a CSV, transforms it using Python, and loads the result into a mock database.

## Structure
- `dags/retail_etl_dag.py`: The Airflow DAG definition
- `scripts/extract.py`: Extract data from a CSV
- `scripts/transform.py`: Transform logic
- `scripts/load.py`: Mock loading into a database
- `requirements.txt`: Python dependencies

## Usage
1. Install requirements from `requirements.txt`.
2. Place your CSV data in `data/retail_data.csv`.
3. Initialize and run Airflow.
4. The DAG `retail_etl_dag` will handle extraction, transformation, and loading.
