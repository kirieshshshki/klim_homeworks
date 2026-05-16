import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
from collections import deque
import time
import matplotlib.pyplot as plt


BASE = "https://ru.wikipedia.org"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (SeminarScraper/1.0; +https://example.org/)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "ru,en;q=0.8",
}


def article_to_url(title: str) -> str:
    return f"{BASE}/wiki/{title.replace(' ', '_')}"


def is_valid_article_href(href: str) -> bool:
    if href.startswith("//ru.wikipedia.org/wiki/"):
        title = href[len("//ru.wikipedia.org/wiki/"):]

    elif href.startswith("/wiki/"):
        title = href[len("/wiki/"):]

    else:
        return False

    if not title:
        return False
    if "#" in title:
        return False
    if ":" in title:
        return False
    if "?" in title:
        return False
    if title.startswith("Заглавная_страница"):
        return False

    return True


def href_to_title(href: str) -> str:
    if href.startswith("//ru.wikipedia.org/wiki/"):
        title = href[len("//ru.wikipedia.org/wiki/"):]

    else:
        title = href[len("/wiki/"):]

    title = unquote(title)
    title = title.replace("_", " ")

    return title


def extract_article_links(article_title: str, max_links: int = 30):
    url = article_to_url(article_title)

    print("сейчас программа на:", url)

    resp = requests.get(url, headers=HEADERS, timeout=20)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")
    content = soup.find("div", id="mw-content-text")

    if content is None:
        return []

    links = []
    seen = set()

    for p in content.find_all("p"):
        for a in p.find_all("a", href=True):
            href = a["href"]

            if not is_valid_article_href(href):
                continue

            title = href_to_title(href)

            if title == article_title:
                continue

            if title in seen:
                continue

            seen.add(title)
            links.append(title)

            if len(links) >= max_links:
                return links

    return links


def get_random_article():
    url = "https://ru.wikipedia.org/api/rest_v1/page/random/summary"

    resp = requests.get(url, headers=HEADERS, timeout=20)
    resp.raise_for_status()

    data = resp.json()
    title = data["title"]

    return title


def find_path_to_article(
    start_title: str,
    target_title: str,
    depth: int = 3,
    max_links_per_page: int = 30,
    sleep_sec: float = 0.2
):
    visited = set()
    queue = deque([(start_title, 0)])
    parent = {start_title: None}

    found_article = None

    while queue:
        current_title, current_depth = queue.popleft()

        if current_title in visited:
            continue

        visited.add(current_title)

        if current_title == target_title:
            found_article = current_title
            break

        if current_depth >= depth:
            continue

        try:
            neighbors = extract_article_links(
                current_title,
                max_links=max_links_per_page
            )
        except Exception as e:
            print(f"Ошибка при обработке статьи '{current_title}': {e}")
            continue

        for nb in neighbors:
            if nb not in parent:
                parent[nb] = current_title
                queue.append((nb, current_depth + 1))

        time.sleep(sleep_sec)

    if found_article is None:
        return None

    path = []

    while found_article is not None:
        path.append(found_article)
        found_article = parent[found_article]

    path.reverse()

    return path


TARGET_ARTICLE = "Демократия"

EXPERIMENTS_COUNT = 3
DEPTH = 3
MAX_LINKS_PER_PAGE = 30
SLEEP_SEC = 0.2

distances = []


for i in range(EXPERIMENTS_COUNT):
    print(f"эксперимент {i + 1}")

    start_article = get_random_article()
    print("стартовая статья:", start_article)

    path = find_path_to_article(
        start_title=start_article,
        target_title=TARGET_ARTICLE,
        depth=DEPTH,
        max_links_per_page=MAX_LINKS_PER_PAGE,
        sleep_sec=SLEEP_SEC
    )

    if path is None:
        print("к сожалению, демократия не нашлась")

    else:
        transitions = len(path) - 1
        distances.append(transitions)

        print("путь:")
        print(" -> ".join(path))
        print("кол-во переходов:", transitions)


print("кол-во запусков:", EXPERIMENTS_COUNT)
print("кол-во успешных запусков:", len(distances))
print("кол-во неуспешных запусков:", EXPERIMENTS_COUNT - len(distances))

if len(distances) > 0:
    print("длина пути до демократии:", distances)

    plt.figure(figsize=(10, 5))

    plt.bar(
        labels,
        distances,
        edgecolor="black",
        color="plum"
    )

    plt.xlabel("номер эксперимента и стартовая статья")
    plt.ylabel("кол-во переходов")
    plt.title("путь к демократии:")

    plt.yticks(range(0, max(distances) + 1))
    plt.xticks(rotation=25, ha="right")

    plt.tight_layout()
    plt.show()

else:
    print("поиграли в демократию и хватит")
