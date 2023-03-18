import csv
import mysql.connector

# Connect to the MySQL server and select the patents database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="patents"
)
cursor = db.cursor()

# cursor.execute("DELETE FROM patents_info")


# Open the CSV file and insert the data into the table
with open('Patents_data.csv', 'r', encoding='ISO-8859-1') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['PUBLICATION_DATE'] == '':
            continue  # skip rows with empty values

        query = """
            INSERT INTO patents_info (
                PUBLICATION_DATE,
                APPLICATION_NUMBER,
                IPO_LOCATION,
                APPLICATION_TYPE_DESC,
                DATE_OF_FILING,
                TITLE_OF_INVENTION,
                FIELD_OF_INVENTION,
                NO_OF_PAGES
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            row['PUBLICATION_DATE'],
            row['APPLICATION_NUMBER'],
            row['IPO_LOCATION'],
            row['APPLICATION_TYPE_DESC'],
            row['DATE_OF_FILING'],
            row['TITLE_OF_INVENTION'],
            row['FIELD_OF_INVENTION'],
            row['NO_OF_PAGES']
        )
        cursor.execute(query, values)


cursor.execute("SELECT * FROM patents_info")
results = cursor.fetchall()

# Print the results
for entries in results:
    print(entries)
# Commit the changes and close the database connection
db.commit()
cursor.close()
db.close()
