import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH")

def save_user_db(user_info) -> None:
    con = sqlite3.connect(os.path.join((str(DB_PATH))))
    cursor = con.cursor()
    insert_stmn = '''
            INSERT INTO USERS (first_name, last_name, username, email, password, skills)
            VALUES (?, ?, ?, ?, ?, ?);
        '''
    cursor.execute(insert_stmn, user_info)
    con.commit()
    cursor.close()
    con.close()
    
def save_company_db(company_info) -> None:
    con = sqlite3.connect(os.path.join((str(DB_PATH))))
    cursor = con.cursor()
    insert_stmn = '''
            INSERT INTO COMPANIES (name, location, cnt_job_ads, cnt_employees, year_founded)
            VALUES (?, ?, ?, ?, ?);
        '''
    cursor.execute(insert_stmn, company_info)
    con.commit()
    cursor.close()
    con.close()


def check_password_username(username, password) -> bool:
    con = sqlite3.connect(os.path.join((str(DB_PATH))))
    cursor = con.cursor()
    
    select = "SELECT password FROM USERS WHERE username = ? and password = ?"
    
    cursor.execute(select, (username, password))
    
    result = cursor.fetchone()
    
    if result:
        return True
    
    return False

def get_all_job_data() -> pd.DataFrame:
    '''
    Get all job ads data
    '''
    conn = sqlite3.connect(os.path.join((str(DB_PATH))))

    query = """
        SELECT j.title, j.date_posted, c.name AS company_name, c.location AS company_location
        FROM JOB_ADS j
        JOIN COMPANIES c ON j.company_id = c.id;
    """
    job_data = pd.read_sql_query(query, conn)
    
    conn.close()

    return job_data


def get_full_data() -> pd.DataFrame:
    '''
    Get full data
    '''
    conn = sqlite3.connect(os.path.join((str(DB_PATH))))

    query = """
        SELECT j.*, c.*
        FROM JOB_ADS j
        JOIN COMPANIES c ON j.company_id = c.id;
    """
    job_data = pd.read_sql_query(query, conn)
    
    conn.close()

    return job_data


def get_all_company_data() -> None:
    conn = sqlite3.connect(os.path.join((str(DB_PATH))))

    query = """
        SELECT c.*
        FROM COMPANIES c;
    """
    job_data = pd.read_sql_query(query, conn)
    
    return job_data

def get_user_skills(username) -> None:
    '''
    Get user skills by username
    '''
    conn = sqlite3.connect(os.path.join((str(DB_PATH))))
    cursor = conn.cursor()
    query = """
        SELECT u.skills
        FROM USERS u WHERE u.username = ?;
    """
    cursor.execute(query, (username,))
    user_skills = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return user_skills

def chnage_password_db(user_info: tuple) -> None:
    con = sqlite3.connect(os.path.join((str(DB_PATH))))
    cursor = con.cursor()
    update_stmn = '''
            UPDATE USERS
            SET password = ?
            WHERE username = ?;
        '''
    cursor.execute(update_stmn, user_info)
    con.commit()
    cursor.close()
    con.close()
    
def get_password_db(username) -> str:
    print(username)
    con = sqlite3.connect(os.path.join((str(DB_PATH))))
    cursor = con.cursor()
    select = "SELECT password FROM USERS WHERE username = ?"
    cursor.execute(select, (username,))
    password = cursor.fetchone()
    cursor.close()
    con.close()
    print(password)
    return password[0]