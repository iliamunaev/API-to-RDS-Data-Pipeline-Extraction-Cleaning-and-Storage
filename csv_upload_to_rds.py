import pandas as pd
from sqlalchemy import create_engine

# Read CSV file
csv_file = 'my_csv_file.csv'
df = pd.read_csv(csv_file)

# Set Database connection parameters
db_port = 5432  # Port by defoult
db_name = 'my_db_name'
db_username = 'my_username'
db_password = 'my_password'

#Establish a connection to RDS instance using SQLAlchemy
engine = create_engine(f'postgresql+psycopg2://{db_username}:{db_password}@{db_endpoint}:{db_port}/{db_name}')

# Write the contents of the DataFrame to the RDS instance
table_name = 'my_table_name'
df.to_sql(table_name, engine, if_exists='replace', index=False)

print('CSV uploaded to Database')
