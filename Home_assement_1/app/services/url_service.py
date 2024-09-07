
from app.utils.web_url_utils.scrapper import scrap_data

def process_url(url):
    scraped_data = scrap_data(url)
    # return {"chat_id":chat_id, "scraped_data":scraped_data}

    return scraped_data