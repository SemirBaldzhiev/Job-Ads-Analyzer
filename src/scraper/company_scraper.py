import requests
import sqlite3
from bs4 import BeautifulSoup
from src.dbsqlite.db_worker import save_company_db
import os
from dotenv import load_dotenv

load_dotenv()
COMPANY_URL = os.getenv("COMPANY_URL")

def extract_company() -> None:
    '''
    Extract all company information
    '''
    response = requests.get(COMPANY_URL)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        all_companies = soup.find_all("div", {"class": "bottom-inner"})
        
        for company in all_companies:
            company_link = company.find("a").get("href")
            extract_company_info(company_link)

def extract_company_info(company_link: str) -> None:
    '''
    Extract specific company information
    '''
    response_company = requests.get(company_link)
            
    if response_company.status_code == 200:
        soup_company = BeautifulSoup(response_company.text, "html.parser")
        company_name = soup_company.find("h1", {"class": "company-heading"})
        
        if company_name is None:
            return
        else:
            company_name = company_name.text.strip()
        company_details = soup_company.find_all("div", {"class": "box-company-info"})
        
        cnt_employees = company_details[1].find("p", {"class": "p-big-18 bold without-margin"}).text.strip().replace("-", "").replace("+", "").split(" ")
        if len(cnt_employees) > 1 and not cnt_employees[0].isnumeric():
            cnt_employees = int("".join(cnt_employees[1:]))
        else:
            cnt_employees = int("".join(cnt_employees))
        
        year_founded = company_details[0].find("p", {"class": "p-big-18 bold without-margin"}).text.strip().split(" ")[0]
        if year_founded.isnumeric():
            year_founded = int(year_founded)
        else:
            year_founded = 0
        
        location = company_details[-2].find("p", {"class": "p-big-18 bold without-margin"}).text.strip()
        cnt_div = soup_company.find("div", {"class": "jobs-number-holder"})
        
        if cnt_div is not None:
            cnt_job_ads = int(cnt_div.find("div").text.strip())
        else:
            cnt_job_ads = 0

        save_company_db((company_name, location, cnt_job_ads, cnt_employees, year_founded))
        


    
if __name__ == "__main__":
    extract_company()