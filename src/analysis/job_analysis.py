import sqlite3
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from src.dbsqlite.db_worker import get_full_data



def wordcloud_job_titles() -> None:
    '''
    Generate a word cloud for job titles with interactive visualization
    '''
    conn = sqlite3.connect('/home/semir/python-project/Job-Ads-Analyzer/src/job_ads.db')

    # Load job data from the database into a DataFrame
    query = """
        SELECT j.*
        FROM JOB_ADS j;
    """
    job_data = pd.read_sql_query(query, conn)

    # Generate a word cloud for job titles
    wordcloud = WordCloud(width=800, height=400, max_words=50, background_color='white').generate(' '.join(job_data['title']))

    # Display the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud for Job Titles')
    plt.show()

    conn.close()


def distribution_by_date_posted() -> None:
    '''
    Generate a distribution plot for the number of job ads by date posted
    '''
    conn = sqlite3.connect('/home/semir/python-project/Job-Ads-Analyzer/src/job_ads.db')

    # Load job data from the database into a DataFrame
    query = """
        SELECT j.date_posted, COUNT(j.id) AS cnt_job_ads
        FROM JOB_ADS j
        GROUP BY j.date_posted;
    """
    job_data = pd.read_sql_query(query, conn)

    # Generate a distribution plot for the number of job ads by date posted
    plt.figure(figsize=(14, 8))
    plt.bar(job_data['date_posted'], job_data['cnt_job_ads'])
    plt.title('Distribution of Job Ads by Date Posted')
    plt.xlabel('Date Posted')
    plt.ylabel('Number of Job Ads')
    plt.xticks(rotation=45)
    plt.show()

    conn.close()
    

def filter_job_ads(job_data, **kwargs) -> None:
    '''
    Filter job ads by different criteria
    '''

    filtered_data = job_data
    for key, value in kwargs.items():
        if value.isnumeric():
            filtered_data = filtered_data[filtered_data[key] == int(value)]
        else:   
            filtered_data = filtered_data[filtered_data[key].str.contains(value, case=False, regex=False)]

    return filtered_data


def sort_ads(data, ascending: bool, *args,):
    '''
    Sort job ads by different criteria
    '''
    
    sorted_data = data.sort_values(list(args), ascending=ascending)
        
    return sorted_data

if __name__ == "__main__":
    pass    