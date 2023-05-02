# API-to-RDS Data Pipeline for NYC High-Value Taxi Trips 2021: Extraction, Cleaning, and Storage
## Step 3: Correction
- Change data type of the columns 
- Read final output
 
#### Change data type of the columns 

```sql
ALTER TABLE ny_taxi
ALTER COLUMN pickup_date TYPE date using ("pickup_date"::text::date),
ALTER COLUMN pickup_time TYPE time using ("pickup_time"::text::time),
ALTER COLUMN dropoff_date TYPE date using ("dropoff_date"::text::date),
ALTER COLUMN dropoff_time TYPE time using ("dropoff_time"::text::time),
ALTER COLUMN passenger_count TYPE smallint,
ALTER COLUMN payment_type TYPE smallint;
```

#### Read the first 5 rows of Database

```sql
SELECT *
FROM ny_taxi
LIMIT 5;
```

<img src="https://github.com/iliamunaev/ny_taxi_data/blob/main/pics/final_result_SQL.png" alt="SQL query output">
