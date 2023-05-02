# Project name
## Step 3:
- Read CSV file
- Set Database connection parameters
- Establish a connection to RDS instance using SQL
- Write the contents of the DataFrame to the RDS instance

#### Read the first 5 rows of Database

SELECT *
FROM ny_taxi
LIMIT 5;


#### Change data type of the columns 

ALTER TABLE ny_taxi
ALTER COLUMN pickup_date TYPE date using ("pickup_date"::text::date),
ALTER COLUMN pickup_time TYPE time using ("pickup_time"::text::time),
ALTER COLUMN dropoff_date TYPE date using ("dropoff_date"::text::date),
ALTER COLUMN dropoff_time TYPE time using ("dropoff_time"::text::time),
ALTER COLUMN passenger_count TYPE smallint,
ALTER COLUMN payment_type TYPE smallint;