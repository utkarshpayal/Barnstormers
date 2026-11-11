# Barnstormers

It is a website which provides Patents data.

![image](https://user-images.githubusercontent.com/104209135/225948027-623ae4a5-1eb0-4303-8d76-d01491d0dbae.png)

Barnstormers loads Indian patent application records from CSV files into a MySQL database and displays them as cards on a web page. It also includes a static "Patent Search" page with search, sort, filter and pagination controls.

## Project Status

This is an early-stage project. The search, sort, filter and pagination handlers in `script.js` are placeholders and are not implemented yet, and `patents.html` does not yet load data from the database.

## Features

- **Database setup** – `database_creation.py` creates a `patents` MySQL database with a `patents_info` table.
- **Data import** – `database_entries.py` reads `Patents_data.csv` and inserts each record (rows with an empty publication date are skipped), then prints the table contents.
- **Patent cards** – `patent_cards.php` queries `patents_info` and renders a card per patent showing the title, publication date, field of invention and application number.
- **Search UI** – `patents.html` + `style.css` + `script.js` provide a keyword search box, a sort dropdown (relevance, publication date, inventor name), filters (assignee, utility/design type) and Prev/Next pagination buttons (UI only for now).

## Tech Stack

- **Python 3** with `mysql-connector-python` (database creation and import)
- **MySQL** (data storage)
- **PHP** with `mysqli` (rendering patent cards)
- **HTML, CSS, JavaScript** (front-end page)

## Project Structure

```
database_creation.py   # Creates the `patents` database and `patents_info` table
database_entries.py    # Imports Patents_data.csv into patents_info
Patents_data.csv       # Patent records imported by database_entries.py
data/                  # Additional patent datasets (2019 applications, 2019 grants, historical counts)
patent_cards.php       # Renders patent records from MySQL as cards
patents.html           # Patent Search page (UI)
script.js              # Event handler stubs for the search page
style.css              # Styles for the search page
```

### Data columns

The `patents_info` table (and `Patents_data.csv`) uses these columns:
`PUBLICATION_DATE`, `APPLICATION_NUMBER` (primary key), `IPO_LOCATION`, `APPLICATION_TYPE_DESC`, `DATE_OF_FILING`, `TITLE_OF_INVENTION`, `FIELD_OF_INVENTION`, `NO_OF_PAGES`.

## Setup

### Prerequisites

- Python 3
- A running MySQL server
- PHP with the `mysqli` extension (for `patent_cards.php`)

### 1. Install the Python dependency

```bash
pip install mysql-connector-python
```

### 2. Configure the database connection

There is no config file or environment variables. The MySQL host, user and password are hard-coded in `database_creation.py`, `database_entries.py` and `patent_cards.php`. Edit the connection settings in those files to match your local MySQL server before running them.

### 3. Create the database and import the data

Run from the repository root (the import script reads `Patents_data.csv` by relative path):

```bash
python database_creation.py
python database_entries.py
```

### 4. View the pages

- Serve the repository with a PHP-capable web server and open `patent_cards.php` to see the patent cards rendered from the database. For example, with PHP's built-in server:

  ```bash
  php -S localhost:8000
  ```

  then visit `http://localhost:8000/patent_cards.php`.
- Open `patents.html` directly in a browser to see the search UI.
