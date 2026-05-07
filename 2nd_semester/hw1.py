import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


headers = {
    "User-Agent": "Mozilla/5.0 (SeminarScraper/1.0; +https://example.org/)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "ru,en;q=0.8",
}

session = requests.Session()
session.headers.update(headers)

BASE = "https://ru.wikipedia.org"
url = "https://ru.wikipedia.org/api/rest_v1/page/random/summary"


resp = session.get(url, timeout=20)
data = resp.json()
title = data["title"]
article_url = data["content_urls"]["desktop"]["page"]

visited = []
visited.append([title, article_url])
print("Первая статья:")
print(title)
print(article_url)


for i in range(2):
    resp_article = session.get(article_url, headers=headers, timeout=20)
    soup_article = BeautifulSoup(resp_article.text, "lxml")
    content = soup_article.find(id="mw-content-text")
    link = content.find_all("a", href=True)
    good_links = []
    for a in link:
        href = a["href"]
        full_url = urljoin(article_url, href)
        if full_url.startswith(BASE + "/wiki/") and "#" not in full_url and "?" not in full_url:
            name = full_url.split("/wiki/")[1]
            if ":" not in name and "%3A" not in name and "%3a" not in name:
                good_links.append(full_url)
    if len(good_links) == 0:
        print("Подходящих ссылок в статье не найдено")
        break

    article_url = good_links[0]
    resp_article = session.get(article_url, headers=headers, timeout=20)
    soup_article = BeautifulSoup(resp_article.text, "lxml")
    title = soup_article.find("h1").get_text(strip=True)
    visited.append([title, article_url])
    print()
    print("Следующая статья:")
    print(title)
    print(article_url)


file = open("странички.txt", "w", encoding="utf-8")
for page in visited:
    file.write(page[0] + "\n")
    file.write(page[1] + "\n")
    file.write("\n")
file.close()
