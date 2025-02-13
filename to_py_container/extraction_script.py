import mysql.connector
from clickhouse_driver import Client

# MySQL connection settings
MYSQL_HOST = "mysql"
MYSQL_USER = "example_user"
MYSQL_PASSWORD = "example_password"
MYSQL_DATABASE = "example_db"

# ClickHouse connection settings
CLICKHOUSE_HOST = "clickhouse"
CLICKHOUSE_DATABASE = "default"
CLICKHOUSE_TABLE = "users"

def basic_tranformation(data):
    """converts all email addresses to lowercase"""

def advanced_transformation(data):
    """creates a column called full_name that concatenates first_name and last_name and drops the first_name and last_name columns"""


def fetch_mysql_data():
    """Fetch all data from the MySQL 'users' table."""
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, first_name, last_name, email FROM users")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def create_clickhouse_table(client):
    """Create the ClickHouse table if it doesn't exist."""
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {CLICKHOUSE_DATABASE}.{CLICKHOUSE_TABLE} (
        id Int32,
        first_name String,
        last_name Int32,
        email String
    )
    ENGINE = MergeTree()
    ORDER BY id
    """
    client.execute(create_table_query)

def insert_data_into_clickhouse(client, data):
    """Insert data into ClickHouse."""
    insert_query = f"INSERT INTO {CLICKHOUSE_DATABASE}.{CLICKHOUSE_TABLE} (id, first_name, last_name, email) VALUES"
    formatted_data = [
        (row['id'], row['first_name'], row['last_name'], row['email']) for row in data
    ]
    client.execute(
        insert_query,
        formatted_data,
        columns=['id', 'first_name', 'last_name', 'email', 'created_at'],
        )

def main():
    """Main function to handle the ETL process."""
    # Fetch data from MySQL
    print("Fetching data from MySQL...")
    mysql_data = fetch_mysql_data()

    # Connect to ClickHouse
    print("Connecting to ClickHouse...")
    client = Client(host=CLICKHOUSE_HOST)

    # Clear the existing data in the table
    print("Clearing existing data in ClickHouse...")
    client.execute(f"DROP TABLE IF EXISTS {CLICKHOUSE_DATABASE}.{CLICKHOUSE_TABLE}")
    
    # Ensure the table exists
    print("Creating table in ClickHouse if it doesn't exist...")
    create_clickhouse_table(client)


    # Insert new data into ClickHouse
    print("Inserting data into ClickHouse...")
    insert_data_into_clickhouse(client, mysql_data)

    print("Data transfer completed successfully.")

if __name__ == "__main__":
    main()
