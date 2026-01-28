# Request BS4 — Django Product Parser

The **request-bs4_TASK** project is a 
Django application for parsing product data from web pages
using **requests + BeautifulSoup4**, storing the results
in a **PostgreSQL** database, and exporting data to **CSV**
via custom Django management commands.

---

##  Features

* Product parsing from web pages (requests + BeautifulSoup4)
* Saving parsed data to PostgreSQL using Django ORM
* Custom Django **management commands**
* Export parsed products to CSV
* Clear separation of business logic using a `services` layer

---

##  Project Structure

```text
JobTask/
├── config/                 # Django project configuration
│   └── config/
│       ├── __init__.py
│       ├── asgi.py
│       ├── settings.py     # Django settings (PostgreSQL configuration)
│       ├── urls.py
│       └── wsgi.py
│
├── products/               # Django application
│   ├── management/
│   │   └── commands/
│   │       ├── parse_product.py   # Command for parsing products
│   │       └── export_csv.py      # Command for CSV export
│   │
│   ├── migrations/
│   ├── services/           # Business logic layer
│   │   ├── parser.py
│   │   └── export_to_csv.py
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py           # Product model
│   ├── tests.py
│   └── views.py
│
├── manage.py
├── products.csv            # Example exported file
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

* Python **3.10+**
* Django **5.2.4**
* PostgreSQL **13+**
* pip / virtualenv

---

## 🚀 How to Run the Project

### 1️ Clone the repository

```bash
git clone https://github.com/NK-TS-DEV/request-bs4_TASK.git
cd config
```

---

### 2️ Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

---

### 3️ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🐘 PostgreSQL Setup

Below are the **actual commands used in this project** to create the database and user:

```PostgreSQL
CREATE USER brain_user WITH PASSWORD '1234';
CREATE DATABASE brain_db OWNER brain_user;
GRANT ALL PRIVILEGES ON DATABASE brain_db TO brain_user;
```

> The user `brain_user` is assigned as the database owner, 
> so no additional role configuration is required.

### Database configuration (`config/settings.py`)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'brain_db',
        'USER': 'brain_user',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

##  Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

##  Management Commands

###  Parse products

```bash
python manage.py parse_product
```

This command:

* sends HTTP requests to target pages
* parses HTML using BeautifulSoup
* saves parsed products to PostgreSQL

---

### 📤 Export products to CSV

```bash
python manage.py export_csv
```

Result:

* `products.csv` file generated in the project root

---

##  Architecture Overview

* **models.py** — database schema
* **services/** — business logic (parser, CSV export)
* **management/commands/** — parser data
* **settings.py** — Django and PostgreSQL configuration



