from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
import re
import time

def get_url_content(url: str):
    
    try:
        response = requests.get(url)
        return response.content
    except RequestException as e:
        raise(f"An error occurred: {e}")


def filter_links(links: list):
  
    url_pattern = re.compile(
        r"https?://(?!.*(?:\.pdf|facebook\.com|twitter\.com|github\.com))\S+"
    )
    unique_links = set()
    for link in links:
        match = re.search(url_pattern, link)
        if match:
            unique_links.add(match.group())
    return list(unique_links)


def fetch_links(page_content):

    soup = BeautifulSoup(page_content, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    links = []
    for link in soup.find_all("a", href=True):
        links.append(link["href"])

    return links


def extract_links(url: str):
   
    page_content = get_url_content(url)
    if page_content:
        links = fetch_links(page_content)
        filtered_links = filter_links(links)
        filtered_links.insert(0,url)
        
        return filtered_links
    

def scrap_data(url):

    filtered_links = extract_links(url)

    scrapped_data = {}

    try:

        for link in filtered_links:

            page_content = get_url_content(link)
            time.sleep(1)
            soup = BeautifulSoup(page_content, 'html.parser')
            
            for script in soup(["script", "style"]):
                script.extract()

            text = soup.get_text().strip()

            scrapped_data[str(url)] = text

            return scrapped_data

    except RequestException as e:
        raise (f"Exception Occur for the url {url} is {e}")

    