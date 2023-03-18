import csv
import mysql.connector

# Connect to the MySQL server and create the database and table
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS patents")
cursor.execute("USE patents")
cursor.execute("""
CREATE TABLE IF NOT EXISTS patents_info (
    PUBLICATION_DATE DATE,
    APPLICATION_NUMBER VARCHAR(50) NOT NULL,
    IPO_LOCATION VARCHAR(50) NOT NULL,
    APPLICATION_TYPE_DESC VARCHAR(150) NOT NULL,
    DATE_OF_FILING DATE NOT NULL,
    TITLE_OF_INVENTION VARCHAR(1000),
    FIELD_OF_INVENTION VARCHAR(50) NOT NULL,
    NO_OF_PAGES INT NOT NULL,
    PRIMARY KEY (APPLICATION_NUMBER)
)
""")

cursor.close()
db.close()
