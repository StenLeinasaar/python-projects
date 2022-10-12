import requests
from bs4 import BeautifulSoup




"""
Web scraping ERR news 
"""
URL = "https://www.err.ee/l/valismaa"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


results = soup.find(class_="left-block")


news_articles = results.find_all("div", class_="category-item")


# This si the article header
# <p class="category-news-header"><a href="https://www.err.ee/1608748276/bloomberg-usa-voib-keelustada-vene-alumiiniumi-sisseveo" target="_self">
# 										Bloomberg: USA võib keelustada Vene alumiiniumi sisseveo									</a></p>


# print(news_articles.prettify())
for article in news_articles:
    # print(article.prettify())
    article_title = article.find("p",class_="category-news-header")
    # print(article_title)
    links = article_title.find("a")
    for link in links:
        print(link.strip())
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     print(title_element.text)
#     print(company_element.text)
#     print(location_element.text)
#     print()