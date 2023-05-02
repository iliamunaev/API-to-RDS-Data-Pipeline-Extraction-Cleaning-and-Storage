# API-to-RDS Data Pipeline for NYC High-Value Taxi Trips 2021: Extraction, Cleaning, and Storage

## Overview

This project aims to create a comprehensive and well-structured database of New York yellow taxi trips in 2021, focusing specifically on trips that cost $50 or more. This database will be a valuable resource for researchers, analysts, and other interested parties seeking to explore and understand the factors influencing high-cost taxi rides in New York City.

Project steps

- Utilizing Python, I will extract relevant taxi trip data from public APIs, focusing on yellow taxi rides in New York City during the year 2021 with a trip cost of $50 or more.
- Once the raw data is collected, it will undergo a thorough cleaning process to remove any errors, inconsistencies, or missing values, ensuring the final dataset is accurate and reliable for further analysis. 
- In the next step, I will create a structured database on Amazon RDS, allowing for easy accessibility, storage, and dataset management.
- Finally, the data will be uploaded to the Amazon RDS database from a CSV file. Some correction will be made in pgAdmin by using SQL.

## Navigation

Step 1: Extraction and cleaning: step by step in [JupyterNotebook](https://github.com/iliamunaev/API-to-RDS-Data-Pipeline-Extraction-Cleaning-and-Storage/blob/main/step1_retrieve_clean_data_python.ipynb), python [code](https://github.com/iliamunaev/API-to-RDS-Data-Pipeline-Extraction-Cleaning-and-Storage/blob/main/retrieve_data_from_API.py).  
Step 2: Upload to Amazon RDS: step by step in [JupyterNotebook](https://github.com/iliamunaev/API-to-RDS-Data-Pipeline-Extraction-Cleaning-and-Storage/blob/main/step2_upload_CSV_to_database_python.ipynb), python [code](https://github.com/iliamunaev/API-to-RDS-Data-Pipeline-Extraction-Cleaning-and-Storage/blob/main/csv_upload_to_rds.py).  
Step 3: Correction (SQL): step by step in [JupyterNotebook](https://github.com/iliamunaev/API-to-RDS-Data-Pipeline-Extraction-Cleaning-and-Storage/blob/main/step3_change_column_types_SQL.md).

## Environment and tools:
- Amazon RDS
- JupyterLab 
- PgAdmin 4
- PostgresSQL 15
- PyCharm
- Python 3.11.3

## Libreries:
- **json** - *built-in package, which can be used to work with JSON data*
- **pandas** - *ibrary written for the Python programming language for data manipulation and analysis)*
- **psycopg2** - *PostgreSQL database adapter for Python*
- **requests** - *allows to send HTTP/1.1 request*
- **sqlalchemy** - *Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL*
- **uuid** - *module, which creats a unique ID*

## Dataset

[2021 Yellow Taxi Trip Data](https://data.cityofnewyork.us/Transportation/2021-Yellow-Taxi-Trip-Data/m6nq-qud6)  

*"These records are generated from the trip record submissions made by yellow taxi Technology Service Providers (TSPs). Each row represents a single trip in a yellow taxi in 2021. The trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts."*

<img src="https://github.com/iliamunaev/Data-from-API-to-AWS-RDS-retrieve-clean-upload/blob/main/pics/dataset_overview.png">
Img source: https://data.cityofnewyork.us/Transportation/2021-Yellow-Taxi-Trip-Data/m6nq-qud6


