import requests
from bs4 import BeautifulSoup




"""
Web scraping ERR news 
"""

def scrape_err():

    URL = "https://www.err.ee/l/valismaa"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="left-block")
    news_articles = results.find_all("div", class_="category-item")
    
    # Collecting the dictioanry elements
    collection_of_dic_el = []
    
    for article in news_articles:
        article_elements = article.find("p",class_="category-news-header")
        # findind all the link elements from the article
        links = article_elements.find_all("a")
        # Extracting href to later redirect.
    
        url = links[0]['href']
        title = links[0].text.strip()
        
        dict_el = {title: url}

        collection_of_dic_el.append(dict_el)
    return collection_of_dic_el



def return_dictionary():

    title_link_dict = {}
    toAdd = scrape_err()

    for dict in toAdd:
        title_link_dict.update(dict)

    return title_link_dict


    