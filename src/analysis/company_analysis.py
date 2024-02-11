import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def distribution_by_cnt_ads():
    
    conn = sqlite3.connect('/home/semir/python-project/Job-Ads-Analyzer/src/job_ads.db')

    query = """
        SELECT c.*
        FROM COMPANIES c;
    """
    job_data = pd.read_sql_query(query, conn)
    company_names = job_data["name"]
        
    employee_counts = job_data["cnt_job_ads"]

    # Creating a bar plot
    plt.figure(figsize=(20, 6))
    plt.bar(company_names, employee_counts, color='blue')
    plt.xlabel('Companies')
    plt.ylabel('Employee Count')
    plt.title('Employee Count of Different Companies')
    plt.xticks([])
    plt.tight_layout()

    plt.show()
    

def distribution_by_date_founded():
    
    conn = sqlite3.connect('/home/semir/python-project/Job-Ads-Analyzer/src/job_ads.db')

    query = """
        SELECT c.*
        FROM COMPANIES c;
    """
    job_data = pd.read_sql_query(query, conn)
    
    company_names = job_data[job_data["year_founded"]!=0]

    company_names = company_names["name"]
        
    company_dates = job_data[job_data["year_founded"]!=0]
    company_dates = company_dates["year_founded"]
    

    # Creating a bar plot
    plt.figure(figsize=(15, 6))
    plt.scatter(company_names, company_dates, color='blue', marker='o', alpha=0.7)
    plt.xlabel("Companies")
    plt.ylabel("Date")
    plt.title("Companies by date founded")
    plt.xticks([])
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    distribution_by_date_founded()