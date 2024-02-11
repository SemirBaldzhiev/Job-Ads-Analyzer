import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH")

sql_jobs = '''
    CREATE TABLE JOB_ADS (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        title VARCHAR(255) NOT NULL,
        description VARCHAR(32704) NOT NULL,
        company_id INTEGER NOT NULL,
        date_posted DATE NOT NULL,
        link VARCHAR(255) NOT NULL,
        skills VARCHAR(255) NOT NULL,
        FOREIGN KEY(company_id) REFERENCES COMPANIES(id)
    );
'''

sql_companies = '''
    CREATE TABLE COMPANIES (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name VARCHAR(255) NOT NULL,
        location VARCHAR(255) NOT NULL,
        cnt_job_ads INTEGER NOT NULL,
        cnt_employees INTEGER NOT NULL,
        year_founded INTEGER NOT NULL
        );
'''

sql_users = '''
    CREATE TABLE USERS (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        username VARCHAR(100) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(256) NOT NULL,
        skills VARCHAR(255)
        );
'''

con = sqlite3.connect(os.path.join((str(DB_PATH))))
cursor = con.cursor()

cursor.execute(sql_companies)
cursor.execute(sql_jobs)
cursor.execute(sql_users)

cursor.close()
con.close()

