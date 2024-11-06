#Fashion Trends Data Engineering Project
This project captures fashion trends data using the Google Trends API, processes it, and stores it in a database for further analysis or visualization. The project is designed with a focus on backend data engineering practices, including automated data pipelines, data transformation, and database management.


##Project Overview
The goal of this project is to capture real-time fashion trends from Google Trends and provide insights into global or regional fashion trends. The project demonstrates various data engineering skills, including data ingestion, transformation, loading (ETL), and automation.

##The project consists of:
Fetching data from the Google Trends API.
Cleaning and transforming the data.
Storing the processed data in a PostgreSQL database (or another database).

##Features
Automated Data Pipeline: Automatically fetch fashion trends data using the Google Trends API at regular intervals.
Data Transformation: Normalize and clean the data for easy analysis.
Database Storage: Store the processed data in a PostgreSQL database (or another SQL-based system).
Data Quality: Perform checks to ensure data quality and integrity before loading into the database.
Optional API: Flask API to expose the processed data for external access or further use in applications.
Automated Scheduling: Use Airflow or cron jobs to automate the pipeline.

##Tech Stack
Languages: Python
Data Fetching: pytrends
Data Processing: pandas
Database: PostgreSQL (or other SQL databases)
Automation: Apache Airflow (or cron jobs) (Soon)
