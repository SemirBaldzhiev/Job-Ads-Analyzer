import sqlite3
import pandas as pd

def save_user_db(user_info):
    con = sqlite3.connect("/home/semir/python-project/Job-Ads-Analyzer/src/job_ads.db")
    cursor = con.cursor()
    insert_stmn = '''
            INSERT INTO USERS (first_name, last_name, username, email, password, skills)
            VALUES (?, ?, ?, ?, ?, ?);
        '''
    cursor.execute(insert_stmn, user_info)
    con.commit()
    cursor.close()
    con.close()
    
def save_company_db(company_info):
    con = sqlite3.connect("../job_ads.db")
    cursor = con.cursor()
    insert_stmn = '''
            INSERT INTO COMPANIES (name, location, cnt_job_ads, cnt_employees, year_founded)
            VALUES (?, ?, ?, ?, ?);
        '''
    cursor.execute(insert_stmn, company_info)
    con.commit()
    cursor.close()
    con.close()


def check_password_username(username, password):
    con = sqlite3.connect("/home/semir/python-project/Job-Ads-Analyzer/src/job_ads.db")
    cursor = con.cursor()
    
    select = "SELECT password FROM USERS WHERE username = ? and password = ?"
    
    cursor.execute(select, (username, password))
    
    result = cursor.fetchone()
    
    if result:
        return True
    
    return False

def get_all_job_data():
    '''
    Get all job ads data
    '''
    conn = sqlite3.connect('/home/semir/python-project/Job-Ads-Analyzer/src/job_ads.db')

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
    conn = sqlite3.connect('/home/semir/python-project/Job-Ads-Analyzer/src/job_ads.db')

    query = """
        SELECT j.*, c.*
        FROM JOB_ADS j
        JOIN COMPANIES c ON j.company_id = c.id;
    """
    job_data = pd.read_sql_query(query, conn)
    
    conn.close()

    return job_data


def get_all_company_data():
    conn = sqlite3.connect('/home/semir/python-project/Job-Ads-Analyzer/src/job_ads.db')

    query = """
        SELECT c.*
        FROM COMPANIES c;
    """
    job_data = pd.read_sql_query(query, conn)
    
    return job_data

