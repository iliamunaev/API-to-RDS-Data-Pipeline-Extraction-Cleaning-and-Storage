# Data API to AWS RDS: retrieve, clean, upload
## Step 3:
- Read CSV file
- Set Database connection parameters
- Establish a connection to RDS instance using SQL
- Write the contents of the DataFrame to the RDS instance


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

![SQL query output]([http://url/to/img.png](https://github.com/iliamunaev/ny_taxi_data/blob/main/pics/final_result_SQL.png))
