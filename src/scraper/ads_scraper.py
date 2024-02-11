import requests
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime
import math
from company_scraper import extract_company_info
import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH")
SITE_URL = os.getenv("SITE_URL")
COMPANY_URL = os.getenv("COMPANY_URL")

con = sqlite3.connect(os.path.join((str(DB_PATH))))
cursor = con.cursor()

def extract_job_ads() -> None:

    response = requests.get(SITE_URL)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", {"class": "category-name"})
        jobs_cnt = soup.find_all("span", {"class": "job-qty"})
        
        extract_jobs(links, jobs_cnt)               
        
    close_connection(cursor, con)
                    
def extract_jobs(links, jobs_cnt) -> None:
    for link, cnt in zip(links, jobs_cnt):
        max_pages = math.ceil(int(cnt.text.strip()) / 20)
        print(max_pages)
        extract_jobs_by_pages(link, max_pages)
        if NUM_ADS == 100:
            return

def extract_jobs_by_pages(link, max_pages: int) -> None:
    for pages_cnt in range(1, max_pages):
            
        if pages_cnt == 1:
            response_job = requests.get(link.get("href"))
        else:
            response_job = requests.get(link.get("href") + f"?_paged={pages_cnt}")    
    
        if response_job.status_code == 200:
            
            soup_job = BeautifulSoup(response_job.content, "html.parser")
            job_items = soup_job.find_all("div", {"class": "job-list-item"})
            
            job_links = get_job_links(job_items)
            
            print(len(job_links))
            extract_jobs_description(job_links)
            if NUM_ADS == 100:
                return
            

def get_job_links(job_items) -> list:
    '''
    Get job ads links
    '''
    job_links = []
    for item in job_items:
        job_div = item.find("div", {"class": "inner-right listing-content-wrap"})
        job_link = job_div.find("a", {"class": "overlay-link ab-trigger"}).get("href")
        job_links.append(job_link)
    return job_links


def extract_jobs_description(job_links) -> None:
    '''
    Extract job ads description
    '''
    global NUM_ADS
    for job_link in job_links:
        print(job_link)
        response_job_descr = requests.get(job_link)
        
        soup_job_decr = BeautifulSoup(response_job_descr.content, "html.parser")
        job_title = soup_job_decr.find("h1", {"class":"job-title ab-title-placeholder ab-cb-title-placeholder"}).text.strip()
        print(job_title)
        company_name = soup_job_decr.find("span", {"class": "company-name"}).text.strip()
        
        time_el = soup_job_decr.find("time")
        date_str = time_el["datetime"]
        
        skills = soup_job_decr.find_all("div", {"class": "component-square-badge"})
        list_skills = extract_skills(skills)

        job_desc = soup_job_decr.find("div", {"class": "job_description"})
        
        if job_desc is None:
            job_desc_str = "No description"
        else:
            job_desc_str = job_desc.text.strip()    
        print(company_name)
        
        company_id = cursor.execute("SELECT id FROM COMPANIES WHERE name = ?", (company_name,)).fetchone()
        
        if company_id is None:
            company_link = company_name.replace(" ", "-").lower()
            extract_company_info(COMPANY_URL + company_link)
            company_id = cursor.execute("SELECT id FROM COMPANIES WHERE name = ?", (company_name,)).fetchone()
        
        if company_id is None: continue
        
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
                        
        save_job_db((job_title, job_desc_str, int(company_id[0]), date, job_link, ", ".join(list_skills), ))
        NUM_ADS += 1
        if NUM_ADS == 100:
            return
        
def extract_skills(skills) -> list:
    '''
    Extract skills from job ad
    '''
    list_skills = []
    for skill in skills:
        skill_name = skill.find("img")["title"]
        list_skills.append(skill_name)
    return list_skills
    
def save_job_db(job_info) -> None:
    '''
    Save job ad in the database
    '''
    insert_stmn = '''
        INSERT INTO JOB_ADS (title, description, company_id, date_posted, link, skills)
        VALUES (?, ?, ?, ?, ?, ?);
    '''
    cursor.execute(insert_stmn, job_info)
    con.commit()

def close_connection(cursor, con) -> None:
    '''
    Close connection to the database
    '''
    cursor.close()
    con.close()


if __name__ == "__main__":
    NUM_ADS = 0
    extract_job_ads()